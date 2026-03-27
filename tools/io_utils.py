from __future__ import annotations

import hashlib
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def suites_dir() -> Path:
    return repo_root() / "suites"


def list_suites() -> list[str]:
    d = suites_dir()
    if not d.exists():
        return []
    return sorted(
        [
            p.stem
            for p in d.glob("*.md")
            if p.is_file() and p.name.lower() != "readme.md"
        ]
    )


def load_suite_text(name_or_path: str) -> tuple[str, Path]:
    p = Path(name_or_path)
    if p.suffix.lower() == ".md" and p.exists():
        text = p.read_text(encoding="utf-8")
        return normalize_prompt(text), p

    p2 = suites_dir() / f"{name_or_path}.md"
    if not p2.exists():
        raise FileNotFoundError(f"Suite not found: {name_or_path!r} (expected {p2})")
    text = p2.read_text(encoding="utf-8")
    return normalize_prompt(text), p2


def normalize_prompt(text: str) -> str:
    # Strip an outer markdown code-fence if present (legacy format).
    s = text.strip()
    if s.startswith("```"):
        lines = s.splitlines()
        if (
            len(lines) >= 3
            and lines[0].startswith("```")
            and lines[-1].strip() == "```"
        ):
            s = "\n".join(lines[1:-1]).strip()
    return s + "\n"


def sha256_text(text: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()
