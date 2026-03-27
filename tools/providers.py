from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Any, Optional

import requests


class ProviderError(RuntimeError):
    pass


@dataclass
class GenerateResult:
    text: str
    raw: Any
    timing_ms_total: int


def _ms_since(t0: float) -> int:
    return int((time.time() - t0) * 1000)


def generate_print(*, prompt: str, **_: Any) -> GenerateResult:
    t0 = time.time()
    # No model call; store prompt only.
    return GenerateResult(text="", raw=None, timing_ms_total=_ms_since(t0))


def generate_ollama(
    *,
    prompt: str,
    model: str,
    system: Optional[str],
    temperature: float,
    max_tokens: int,
    timeout_s: int,
) -> GenerateResult:
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
    url = f"{host}/api/chat"

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        },
    }

    t0 = time.time()
    r = requests.post(url, json=payload, timeout=timeout_s)
    if r.status_code >= 400:
        raise ProviderError(f"Ollama error {r.status_code}: {r.text[:500]}")
    raw = r.json()
    text = (raw.get("message") or {}).get("content") or ""
    return GenerateResult(text=text, raw=raw, timing_ms_total=_ms_since(t0))


def generate_openai(
    *,
    prompt: str,
    model: str,
    system: Optional[str],
    temperature: float,
    max_tokens: int,
    timeout_s: int,
) -> GenerateResult:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ProviderError("OPENAI_API_KEY is not set")

    base = os.getenv("OPENAI_BASE_URL", "https://api.openai.com").rstrip("/")
    url = f"{base}/v1/chat/completions"

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    t0 = time.time()
    r = requests.post(url, json=payload, headers=headers, timeout=timeout_s)
    if r.status_code >= 400:
        raise ProviderError(f"OpenAI error {r.status_code}: {r.text[:500]}")
    raw = r.json()
    try:
        text = raw["choices"][0]["message"]["content"]
    except Exception as e:
        raise ProviderError(f"OpenAI response parse error: {e}; raw={str(raw)[:500]}")
    return GenerateResult(text=text or "", raw=raw, timing_ms_total=_ms_since(t0))


def generate_anthropic(
    *,
    prompt: str,
    model: str,
    system: Optional[str],
    temperature: float,
    max_tokens: int,
    timeout_s: int,
) -> GenerateResult:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ProviderError("ANTHROPIC_API_KEY is not set")

    url = "https://api.anthropic.com/v1/messages"
    payload: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        payload["system"] = system

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    t0 = time.time()
    r = requests.post(url, json=payload, headers=headers, timeout=timeout_s)
    if r.status_code >= 400:
        raise ProviderError(f"Anthropic error {r.status_code}: {r.text[:500]}")
    raw = r.json()
    # content is a list of blocks; extract text blocks.
    blocks = raw.get("content") or []
    texts: list[str] = []
    for b in blocks:
        if isinstance(b, dict) and b.get("type") == "text":
            texts.append(b.get("text") or "")
    text = "".join(texts)
    return GenerateResult(text=text, raw=raw, timing_ms_total=_ms_since(t0))
