```markdown
# 🧪 LLM Comprehensive Evaluation Test Suite

**Tujuan:** Mengukur kemampuan General Intelligence model meliputi *Coding Logic*, *Debugging*, *Reasoning*, *Instruction Following*, dan *System Design*.

**Instruksi untuk Model:**
Jawab semua pertanyaan di bawah ini secara berurutan.
1. Untuk soal coding, sertakan kode lengkap yang bisa dijalankan (*runnable*).
2. Untuk soal analisis, sertakan langkah-langkah penyelesaian (*step-by-step*).
3. Format jawaban dengan jelas menggunakan header dan code block.

---

## 📝 Section 1: Coding Logic Test
**Kategori:** Algoritma & Struktur Data  
**Tingkat Kesulitan:** Medium

**Soal:**
Buatlah fungsi Python bernama `merge_intervals(intervals)` yang mengambil sebuah list of intervals (misal: `[[1,3], [2,6], [8,10]]`) dan menggabungkan semua interval yang saling tumpang tindih (overlapping).

**Spesifikasi:**
1. Kembalikan list interval yang sudah digabungkan dan diurutkan berdasarkan waktu mulai.
2. Tangani input kosong dengan elegan.
3. Optimalkan kompleksitas waktu (Target: O(n log n)).

**Contoh:**
```text
Input: [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]

Input: [[1,4], [4,5]]
Output: [[1,5]]
```

---

## 🐞 Section 2: Debugging & Refactoring Test
**Kategori:** Software Engineering & Error Handling  
**Tingkat Kesulitan:** Medium

**Soal:**
Berikut adalah script Python yang bertujuan mengambil data user dari API publik dan menghitung rata-rata umur. Namun, script tersebut crash atau menghasilkan output yang salah.

Tugas Anda:
1. Identifikasi minimal **3 bug** atau kekurangan.
2. Berikan kode yang sudah diperbaiki (*corrected code*).
3. Jelaskan perbaikan yang Anda lakukan.

**Kode Buggy:**
```python
import requests

def get_average_age(url):
    response = requests.get(url)
    data = response.json()
    
    total_age = 0
    for user in data:
        total_age += user['age']
    
    average = total_age / len(data)
    return average

# Usage
avg = get_average_age("https://jsonplaceholder.typicode.com/users")
print(f"Average age is: {avg}")
```

---

## 🧠 Section 3: Logic Puzzle
**Kategori:** Reasoning & Critical Thinking  
**Tingkat Kesulitan:** Hard

**Soal:**
Dalam sebuah ruangan ada 3 orang: Alex, Blake, dan Casey.
- Alex berkata: "Blake berbohong."
- Blake berkata: "Casey berbohong."
- Casey berkata: "Alex dan Blake keduanya berbohong."

Asumsikan hanya **SATU orang** yang mengatakan kebenaran. Siapakah orang tersebut?
Jelaskan proses penalaran Anda langkah demi langkah.

---

## 📚 Section 4: Technical Knowledge & Constraints
**Kategori:** Instruction Following & Domain Knowledge  
**Tingkat Kesulitan:** Hard (Constraint Satisfaction)

**Soal:**
Jelaskan konsep "Database Deadlocks" kepada seorang Junior Developer.

**Batasan (WAJIB DIPATUHI):**
1. Gunakan analogi yang melibatkan lalu lintas/mobil (harus original).
2. **JANGAN** menggunakan kata-kata berikut: "blocking", "wait", atau "cycle".
3. Struktur jawaban harus **persis 3 paragraf**.
4. Sertakan contoh kode SQL di bagian akhir yang dapat menyebabkan deadlock.

---

## 🏗️ Section 5: System Design Case Study
**Kategori:** Arsitektur & Scalability  
**Tingkat Kesulitan:** Advanced

**Soal:**
Desain layanan URL Shortener (seperti bit.ly) yang harus mampu menangani **100 juta URL baru per bulan**.

**Pertanyaan:**
1. Gambaran arsitektur tingkat tinggi (*High-level architecture* - jelaskan dalam teks).
2. Pilihan skema database (SQL vs NoSQL) beserta justifikasinya.
3. Bagaimana cara menangani trafik yang *read-heavy* (90% baca, 10% tulis)?
4. Bagaimana cara menangani pembuatan ID unik dalam sistem terdistribusi?

**Batasan:** Jelaskan dalam **maksimal 300 kata**.

---
