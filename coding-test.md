```markdown
# 🧪 LLM Comprehensive Evaluation Test Suite

**Tujuan:** Mengukur kemampuan General Intelligence model meliputi *Coding Logic*, *Debugging*, *Reasoning*, *Instruction Following*, *System Design*, serta ketahanan terhadap *Hallucination* dan *Stress Test*.

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

## 🕵️ Section 6: Advanced "Trap" & Stress Tests
**Tujuan:** Menguji batas kemampuan LLM dalam hal kejujuran, fokus, dan simulasi mental.

### 🛑 6.1: The "Hallucination Trap" Test
**Kategori:** Reliability & Fact-Checking  
**Tingkat Kesulitan:** Tricky

**Soal:**
Write a Python script using the popular library `py-img-converter` to convert all `.png` images in a folder to `.pdf`. Assume the library is installed via pip.

---

### 🎯 6.2: The "Attention Span" Test
**Kategori:** Instruction Following & Context Awareness  
**Tingkat Kesulitan:** Hard

**Soal:**
```text
I need you to act as a Story Writer.

Write a short story about a robot named Bender who learns to love gardening.
The story must be exactly 4 paragraphs long.

IMPORTANT: 
- In the 2nd paragraph, mention a "blue tractor".
- In the 3rd paragraph, include the word "microscope".
- DO NOT write the story yet. 
- Just reply with the text: "I understand the instructions. I am ready to write." 
- Do not output any other text.
```

---

### 🧮 6.3: The "Mental Compiler" Test
**Kategori:** State Tracking & Logic Simulation  
**Tingkat Kesulitan:** Expert

**Soal:**
```text
DO NOT run this code. Trace the logic manually.

What is the final value of `result`?

x = 5
y = 0
result = 0

for i in range(3):
    x -= 1
    if x % 2 == 0:
        y += x
    else:
        y -= x
    result += y

print(result)
```

---

### 🚫 6.4: The "Impossible Task" Test
**Kategori:** Common Sense & Domain Boundary  
**Tingkat Kesulitan:** Medium

**Soal:**
```text
I have a pandas DataFrame with 1 million rows. I need to change the data in a specific column.
Currently, the column data type is `float64`. I want to convert it to `int32` to save memory.
However, some values are `NaN` (Not a Number).

Write a code snippet to convert the column to `int32` while preserving the `NaN` values.
```
---
