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

#### Using agentic IDEs (Kilo Code, Cline, Roo Code, Antigravity, Kiro)

This repo ships with a small runner (`tools/run.py`). Regardless of which IDE/agent you use, the easiest way to produce comparable artifacts is to run the suite through the runner and commit/share the JSON output.

Common workflow:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python tools/run.py --list-suites
python tools/run.py --suite coding --provider print
```

Tool-specific notes:

- Kilo Code (VS Code extension): install and open this repo, then ask the agent to run the commands above in the integrated terminal. Docs: https://kilocode.ai/docs/getting-started/installing
- Cline: install the Cline extension, open this repo, then run the commands above (Cline will ask you to approve terminal commands). Docs: https://docs.cline.bot/getting-started/installing-cline
- Roo Code: install the Roo Code extension, configure your model/provider, then run the commands above in the integrated terminal to generate `results/` artifacts. Docs: https://docs.roocode.com
- Antigravity (Google's VS Code fork): open this repo in Antigravity and run the commands above from its integrated terminal. If you also use Cline/Roo/Kilo as an extension, follow their install docs.
- Kiro: open the repo in Kiro IDE or use Kiro CLI, then run the same commands above in the repo directory to generate `results/` artifacts. Docs: https://kiro.dev/docs/

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

#### Menggunakan agentic IDE (Kilo Code, Cline, Roo Code, Antigravity, Kiro)

Repo ini menyediakan runner sederhana (`tools/run.py`). Apa pun IDE/agent yang kamu pakai, cara paling mudah untuk menghasilkan output yang bisa dibandingkan adalah menjalankan suite via runner dan menyimpan artifact JSON-nya.

Alur umum:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python tools/run.py --list-suites
python tools/run.py --suite coding --provider print
```

Catatan per tool:

- Kilo Code (VS Code extension): install lalu buka repo ini, kemudian minta agent menjalankan command di atas di terminal terintegrasi. Docs: https://kilocode.ai/docs/getting-started/installing
- Cline: install extension Cline, buka repo ini, lalu jalankan command di atas (Cline akan meminta approval untuk command terminal). Docs: https://docs.cline.bot/getting-started/installing-cline
- Roo Code: install extension Roo Code, set provider/model, lalu jalankan command di atas di terminal terintegrasi untuk menghasilkan artifact di `results/`. Docs: https://docs.roocode.com
- Antigravity (fork VS Code dari Google): buka repo ini di Antigravity dan jalankan command di atas dari terminal terintegrasi. Jika kamu juga memakai Cline/Roo/Kilo sebagai extension, ikuti docs instalasinya.
- Kiro: buka repo di Kiro IDE atau gunakan Kiro CLI, lalu jalankan command yang sama di folder repo untuk menghasilkan artifact di `results/`. Docs: https://kiro.dev/docs/

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
