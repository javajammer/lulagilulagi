from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# When executed as `python tools/run.py`, sys.path[0] is `tools/`.
# Insert repo root so `import tools.*` works consistently.
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    # dotenv is optional; env vars can be set via shell.
    pass

from tools.io_utils import list_suites, load_suite_text, repo_root, sha256_text
from tools.providers import (
    ProviderError,
    generate_anthropic,
    generate_ollama,
    generate_openai,
    generate_print,
)


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_slug(s: str) -> str:
    s2 = re.sub(r"[^a-zA-Z0-9._-]+", "-", s).strip("-")
    return s2[:120] if s2 else "run"


def _build_output_path(
    *, out_dir: Path, suite_name: str, provider: str, model: str
) -> Path:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = out_dir / ts
    run_dir.mkdir(parents=True, exist_ok=True)
    base = "__".join(
        [_safe_slug(suite_name), _safe_slug(provider), _safe_slug(model or "")]
    ).strip("_")
    return run_dir / f"{base}.json"


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Run LLM evaluation prompt suites")
    p.add_argument(
        "--list-suites", action="store_true", help="List available suite names"
    )
    p.add_argument("--suite", help="Suite name (e.g. coding) or path to a .md file")
    p.add_argument(
        "--provider",
        default="print",
        choices=["print", "ollama", "openai", "anthropic"],
        help="Provider backend",
    )
    p.add_argument("--model", default="", help="Model name for the provider")
    p.add_argument("--system", default="", help="Optional system prompt")
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--max-tokens", type=int, default=2048)
    p.add_argument("--timeout", type=int, default=120, help="HTTP timeout in seconds")
    p.add_argument(
        "--output-dir", default="results", help="Directory to store result artifacts"
    )
    args = p.parse_args(argv)

    if args.list_suites:
        for s in list_suites():
            print(s)
        return 0

    if not args.suite:
        p.error("--suite is required (or use --list-suites)")

    suite_text, suite_path = load_suite_text(args.suite)
    suite_name = (
        Path(args.suite).stem if str(args.suite).endswith(".md") else str(args.suite)
    )
    suite_hash = sha256_text(suite_text)

    provider = args.provider
    model = args.model

    if provider != "print" and not model:
        p.error("--model is required for provider != print")

    system: Optional[str] = args.system.strip() or None
    out_dir = (repo_root() / args.output_dir).resolve()

    cmd = " ".join(shlex.quote(x) for x in [sys.executable, "tools/run.py", *argv])
    request_meta: dict[str, Any] = {
        "suite": {
            "name": suite_name,
            "path": str(suite_path),
            "sha256": suite_hash,
        },
        "provider": provider,
        "model": model,
        "params": {
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "timeout_s": args.timeout,
            "system": system or "",
        },
        "tool": {
            "command": cmd,
            "cwd": str(repo_root()),
            "created_at": _utc_now_iso(),
            "version": "0.1.0",
        },
    }

    t0 = time.time()
    try:
        if provider == "print":
            gen = generate_print(prompt=suite_text)
        elif provider == "ollama":
            gen = generate_ollama(
                prompt=suite_text,
                model=model,
                system=system,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                timeout_s=args.timeout,
            )
        elif provider == "openai":
            gen = generate_openai(
                prompt=suite_text,
                model=model,
                system=system,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                timeout_s=args.timeout,
            )
        elif provider == "anthropic":
            gen = generate_anthropic(
                prompt=suite_text,
                model=model,
                system=system,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                timeout_s=args.timeout,
            )
        else:
            raise ProviderError(f"Unsupported provider: {provider}")
    except ProviderError as e:
        total_ms = int((time.time() - t0) * 1000)
        out_path = _build_output_path(
            out_dir=out_dir, suite_name=suite_name, provider=provider, model=model
        )
        payload = {
            "id": str(uuid.uuid4()),
            "created_at": _utc_now_iso(),
            "status": "error",
            "error": str(e),
            "timing_ms": {"total": total_ms},
            "prompt": suite_text,
            "meta": request_meta,
        }
        out_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8"
        )
        print(f"ERROR: {e}")
        print(f"Wrote: {out_path}")
        return 2

    total_ms = int((time.time() - t0) * 1000)
    out_path = _build_output_path(
        out_dir=out_dir, suite_name=suite_name, provider=provider, model=model
    )
    payload = {
        "id": str(uuid.uuid4()),
        "created_at": _utc_now_iso(),
        "status": "ok",
        "timing_ms": {
            "total": total_ms,
            "provider_total": gen.timing_ms_total,
        },
        "prompt": suite_text,
        "response": {
            "text": gen.text,
            "raw": gen.raw,
        },
        "meta": request_meta,
        "env": {
            "OPENAI_BASE_URL": os.getenv("OPENAI_BASE_URL", ""),
            "OLLAMA_HOST": os.getenv("OLLAMA_HOST", ""),
        },
    }
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8"
    )
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
