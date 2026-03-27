# Contributing

This repository accepts new evaluation suites and improvements to the tooling.

## Adding a new suite

1. Create a new Markdown file under `suites/` (e.g. `suites/reasoning.md`).
2. Make the file a single, self-contained prompt that can be sent to a model as-is.
3. Prefer deterministic instructions (explicit output formats, explicit constraints).
4. Avoid copyrighted content, personal data, or secrets.

## Style guide for prompts

- Use clear sections and explicit scoring keys when possible.
- Include an output format block if the answer structure matters.
- Keep dependencies out of prompts (e.g. avoid referencing private libraries).

## Tooling changes

- Keep `tools/run.py` provider-agnostic and add providers via `tools/providers.py`.
- Add minimal dependencies only.
