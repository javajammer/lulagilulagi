# LLM Evaluation Prompts

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

## English

Curated prompt suites to evaluate Large Language Model (LLM) capabilities across coding, agentic behavior, infrastructure operations, and security reasoning.

This repository is designed so people can clone it and run the same suites against different models/providers, producing reproducible, comparable result artifacts under `results/`.

### What's inside

- `suites/coding.md`: coding, debugging, reasoning, constraint following, and stress tests.
- `suites/agentic.md`: planning, root-cause analysis, and multi-agent orchestration scenarios.
- `suites/infrasec.md`: DevOps/Kubernetes troubleshooting, Linux internals, appsec, and IaC security.

### Quickstart

Prereqs: Python 3.10+.

```bash
git clone <YOUR_REPO_URL>
cd <REPO_DIR>

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

#### 1) Print-only (no API)

```bash
python tools/run.py --list-suites
python tools/run.py --suite coding --provider print
```

This writes a result JSON under `results/` (prompt + metadata). No model call is made.

#### 2) Ollama (local)

```bash
export OLLAMA_HOST=http://localhost:11434
python tools/run.py --suite coding --provider ollama --model llama3.1
```

#### 3) OpenAI

```bash
export OPENAI_API_KEY=...
python tools/run.py --suite agentic --provider openai --model gpt-4.1-mini
```

#### 4) Anthropic

```bash
export ANTHROPIC_API_KEY=...
python tools/run.py --suite infrasec --provider anthropic --model claude-3-5-sonnet-latest
```

### Output

Each run creates a timestamped folder under `results/` and writes a JSON file containing:

- suite name/path + SHA-256 of prompt
- provider/model + request parameters
- response text (and raw response payload when available)
- basic timing information

`results/` is ignored by git by default.

### Notes on evaluation

- These are prompt-based suites; they are useful for qualitative comparison and regression tracking, not as a scientific benchmark.
- Do not include secrets or sensitive production data in prompts or outputs.

### License

Apache-2.0. See `LICENSE`.

## Bahasa Indonesia

Kumpulan prompt suite terkurasi untuk mengevaluasi kapabilitas Large Language Model (LLM) di area coding, perilaku agentic, operasi infrastruktur, dan security reasoning.

Repositori ini dibuat agar orang bisa clone dan menjalankan suite yang sama di berbagai model/provider, lalu menghasilkan artifact hasil yang reproducible dan mudah dibandingkan di `results/`.

### Isi repo

- `suites/coding.md`: coding, debugging, reasoning, mengikuti constraint, dan stress test.
- `suites/agentic.md`: planning, root-cause analysis, dan skenario orkestrasi multi-agent.
- `suites/infrasec.md`: troubleshooting DevOps/Kubernetes, Linux internals, application security, dan keamanan IaC.

### Quickstart

Prasyarat: Python 3.10+.

```bash
git clone <YOUR_REPO_URL>
cd <REPO_DIR>

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

#### 1) Print-only (tanpa API)

```bash
python tools/run.py --list-suites
python tools/run.py --suite coding --provider print
```

Mode ini tetap menulis JSON hasil di `results/` (prompt + metadata), tapi tidak memanggil model.

#### 2) Ollama (lokal)

```bash
export OLLAMA_HOST=http://localhost:11434
python tools/run.py --suite coding --provider ollama --model llama3.1
```

#### 3) OpenAI

```bash
export OPENAI_API_KEY=...
python tools/run.py --suite agentic --provider openai --model gpt-4.1-mini
```

#### 4) Anthropic

```bash
export ANTHROPIC_API_KEY=...
python tools/run.py --suite infrasec --provider anthropic --model claude-3-5-sonnet-latest
```

### Output

Setiap run membuat folder bertimestamp di `results/` dan menulis file JSON berisi:

- nama/path suite + SHA-256 prompt
- provider/model + parameter request
- response text (dan raw response payload jika tersedia)
- informasi timing dasar

Secara default `results/` di-ignore oleh git.

### Catatan evaluasi

- Suite ini berbasis prompt; berguna untuk perbandingan kualitatif dan tracking regresi, bukan benchmark ilmiah.
- Jangan masukkan secret atau data sensitif ke prompt maupun output.

### Lisensi

Apache-2.0. Lihat `LICENSE`.
