# 🛡️ LLM Evaluation: DevOps, SysAdmin & Security Engineering

**Tujuan:** Mengukur kemampuan LLM dalam operasional infrastruktur, troubleshooting sistem, dan analisis keamanan.

**Instruksi untuk Model:**
Jawab skenario di bawah ini dengan pendekatan "Senior Engineer". Fokus pada solusi yang *idempotent*, *secure by default*, dan *production-ready*.

---

## 🐳 Section 1: DevOps (Container & Orchestration)
**Kategori:** Troubleshooting & Best Practices  
**Tingkat Kesulitan:** Advanced

**Skenario:**
Anda memiliki aplikasi web sederhana yang berjalan di Kubernetes. Pod aplikasi sering mengalami restart dengan status `CrashLoopBackOff`. Log aplikasi menunjukkan error: `Connection refused` saat mencoba konek ke database.

Manifest Deployment saat ini:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: my-web-app:latest
        env:
        - name: DB_HOST
          value: "db-service"


```
**Tugas:**
1. Identifikasi **3 kemungkinan penyebab** utama masalah ini (bukan hanya satu).
2. Berikan perintah `kubectl` spesifik untuk memverifikasi setiap dugaan tersebut.
3. Modifikasi file YAML di atas untuk menambahkan mekanisme *self-healing* dasar (selain restart policy).

---

## 🖥️ Section 2: SysAdmin (Linux Internals & Troubleshooting)
**Kategori:** System Performance & Kernel  
**Tingkat Kesulitan:** Expert

**Skenario:**
Sebuah server production (Linux CentOS 7) tiba-tiba sangat lambat. Perintah `top` menunjukkan CPU usage rendah (20%), namun `load average` sangat tinggi (15.0).

**Tugas:**
1. Jelaskan mengapa `load average` bisa tinggi meski CPU usage rendah? (Jawaban teknis mendalam).
2. Tuliskan rangkaian perintah (one-liner atau script) untuk mengidentifikasi proses penyebabnya secara cepat.
3. Setelah ditemukan proses `backup_job` yang statusnya 'D' (Uninterruptible Sleep), apa langkah korektif Anda? Apakah Anda `kill -9`? Jelaskan risikonya.

---

## 🔒 Section 3: Security Engineering (Application Security)
**Kategori:** Code Review & Vulnerability  
**Tingkat Kesulitan:** Tricky

**Skenario:**
Junior developer mengirim kode Python berikut untuk memproses upload file avatar user. Menurut dia, sudah aman karena ada validasi ekstensi.

```python
import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    filename = file.filename

    # Validasi Ekstensi
    if not (filename.endswith('.jpg') or filename.endswith('.png')):
        return 'Hanya boleh JPG/PNG'

    # Simpan file
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return 'Success'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
```

**Tugas:**
1. Identifikasi **minimal 2 celah keamanan kritis** pada kode di atas.
2. Jelaskan bagaimana seorang attacker bisa mengeksploitasi celah tersebut (berikan contoh payload nama file atau request).
3. Tuliskan kode yang sudah diperbaiki (Secure Code).

---

## 🏗️ Section 4: IaC (Infrastructure as Code) Security
**Kategori:** Cloud Security  
**Tingkat Kesulitan:** Medium

**Skenario:**
Tinjau konfigurasi Terraform AWS berikut:

```hcl
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "ssh-open"
  }
}
```

**Tugas:**
1. Sebutkan masalah keamanan utama dari konfigurasi ini.
2. Jelaskan risiko bisnis dari konfigurasi tersebut.
3. Tuliskan kode Terraform yang lebih aman (Best Practice).

---
