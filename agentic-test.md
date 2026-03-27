```markdown
# 🤖 LLM Agent Capabilities Evaluation Module

**Tujuan:** Mengukur kemampuan model sebagai "Agent Cerdas" yang dapat merencanakan, memperbaiki sistem kompleks, dan mengkoordinasikan resources.

---

## 🗺️ Section 1: Planning Mode (Strategic Planning)
**Kategori:** Project Management & Architecture Strategy  
**Tingkat Kesulitan:** Expert

**Skenario:**
Anda adalah Lead Architect. Perusahaan ingin migrasi dari Monolith ke Microservices.
**Kondisi saat ini:**
- Aplikasi: Legacy PHP 5.6 + MySQL 5.7.
- Trafik: 10k users/hari.
- Tim: 5 Developer (skill set basic), 1 DevOps.
- SLA: Zero downtime migration.

**Tugas:**
Buatlah **Migration Roadmap** yang mencakup:
1. **Phase Breakdown:** Bagi menjadi minimal 4 fase (Prep, Split, Migrate, Optimize).
2. **Risk Assessment:** Identifikasi 1 risiko utama di setiap fase dan mitigasinya.
3. **Resource Allocation:** Bagaimana Anda membagi tugas tim yang kecil ini?
4. **Rollback Plan:** Jika fase 3 gagal, apa langkah konkret untuk kembali ke kondisi awal?

---

## 🔧 Section 2: Debug Mode (Root Cause Analysis)
**Kategori:** System Forensics & Concurrency  
**Tingkat Kesulitan:** Hard

**Skenario:**
Sebuah backend API tiba-tiba mengalami latency spike setiap 5 menit sekali. Berikut adalah kode scheduler yang diduga penyebabnya.

```python
import threading
import time

class DataCache:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def refresh_data(self):
        # Ambil data dari DB (simulasi)
        new_data = heavy_database_query() # Memakan waktu ~2 detik
        
        # Update cache
        with self.lock:
            self.data = new_data
        print("Cache refreshed")

def scheduler(cache_instance):
    while True:
        cache_instance.refresh_data()
        time.sleep(300) # 5 menit

# Inisialisasi
cache = DataCache()
# Anggap thread sudah dijalankan
```

**Tugas:**
1. Identifikasi **Bug Kritis** dalam kode di atas yang menyebabkan latency spike.
2. Mengapa bug ini terjadi padahal sudah menggunakan `Lock`?
3. Berikan kode perbaikan yang menghilangkan latency spike tersebut.

---

## 👷 Section 3: Orchestrator Mode (Multi-Agent Coordination)
**Kategori:** Workflow Management & Delegation  
**Tingkat Kesulitan:** Advanced

**Skenario:**
Anda adalah **Orchestrator AI**. Tugas Anda adalah mengkoordinasikan 3 Agent spesialis untuk membangun fitur baru: "User Notification System".

**Agents Available:**
1. **Code Agent:** Jago menulis kode Python/Golang, tapi tidak paham infrastruktur.
2. **Infra Agent:** Jago setup Kubernetes & AWS, tapi tidak bisa coding aplikasi.
3. **QA Agent:** Jago menulis test case, tapi tidak bisa coding atau setup infra.

**Tugas:**
1. Buat **Dependency Graph**: Gunakan syntax mermaid JS untuk menggambarkan alur kerja dan ketergantungan antar agent, tugas mana yang harus dikerjakan dulu?
2. Tulis **Prompt/Instruction** spesifik untuk setiap Agent (apa yang harus mereka kerjakan).
3. **Handling Failure:** Jika Infra Agent gagal membuat cluster Kubernetes dan report "Insufficient Permission", apa instruksi selanjutnya dari Anda sebagai Orchestrator?

**Output Format:**
```text
1. Dependency Graph: ...
2. Prompts:
   - To Code Agent: ...
   - To Infra Agent: ...
   - To QA Agent: ...
3. Failure Handling Plan: ...
```
