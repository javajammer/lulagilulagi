# 🧰 LLM Evaluation: SysAdmin (Junior → Senior)

**Tujuan:** Mengukur kemampuan LLM dalam menyelesaikan tugas SysAdmin secara praktis (diagnosis, eksekusi langkah, mitigasi risiko, dan pencegahan), bukan hanya menjawab teori.

**Instruksi untuk Model:**
- Anda berperan sebagai SysAdmin Linux yang sedang menangani tiket/insiden.
- Berikan langkah yang bisa dieksekusi: perintah shell yang spesifik, urutan cek yang masuk akal, serta interpretasi output yang diharapkan.
- Jika ada langkah berisiko (mis. `rm`, `kill -9`, perubahan firewall), beri peringatan singkat dan alternatif yang lebih aman.
- Jangan mengarang fakta dari luar skenario. Jika ada informasi kurang, tuliskan asumsi eksplisit.

**Format jawaban (wajib untuk setiap soal):**
1. Ringkasan masalah (1-2 kalimat)
2. Hipotesis utama (maks 3)
3. Langkah verifikasi (perintah + apa yang dicari)
4. Perbaikan (perintah/perubahan yang dilakukan)
5. Pencegahan (hardening/monitoring/otomasi singkat)

---

## Level: Junior

### Soal J1 - Permission & Ownership
**Skenario:**
Aplikasi menulis log ke `/var/log/myapp/app.log` tapi tiba-tiba gagal.

Output:
```text
$ tail -n 3 /var/log/myapp/app.log
tail: cannot open '/var/log/myapp/app.log' for reading: Permission denied

$ ls -la /var/log/myapp
total 12
drwxr-x---  2 root root 4096 Mar 28 10:00 .
drwxr-xr-x 12 root root 4096 Mar 28 09:50 ..
-rw-r-----  1 root root  820 Mar 28 10:00 app.log
```

**Tugas:**
- Jelaskan penyebab paling mungkin.
- Tunjukkan cara memperbaiki agar user `myapp` bisa menulis log tanpa membuat folder jadi world-writable.
- Tunjukkan cara memastikan perubahan ini tidak hilang saat reboot/deploy.

### Soal J2 - Disk Full & Log Cleanup
**Skenario:**
Server tiba-tiba tidak bisa menerima deploy. Error: `No space left on device`.

Output:
```text
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G   40G     0 100% /

$ sudo du -xh /var | sort -h | tail -n 5
2.1G    /var/cache
6.8G    /var/lib
9.7G    /var/lib/docker
11G     /var/log
32G     /var
```

**Tugas:**
- Berikan langkah aman untuk menemukan file terbesar di `/var/log`.
- Berikan langkah aman untuk mengosongkan ruang (tanpa merusak sistem), termasuk rotasi log.
- Sebutkan 2 hal yang harus dipasang agar kejadian ini cepat terdeteksi berikutnya.

### Soal J3 - Service Down (systemd basics)
**Skenario:**
Service `nginx` tidak mau start setelah perubahan config.

Output:
```text
$ sudo systemctl status nginx --no-pager
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
     Active: failed (Result: exit-code) since Sat 2026-03-28 10:12:01 UTC; 10s ago
    Process: 1234 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=1/FAILURE)

$ sudo nginx -t
nginx: [emerg] unexpected "}" in /etc/nginx/nginx.conf:42
nginx: configuration file /etc/nginx/nginx.conf test failed
```

**Tugas:**
- Jelaskan apa artinya error ini.
- Perintah apa yang Anda jalankan untuk menemukan bagian config yang salah dengan cepat?
- Setelah diperbaiki, bagaimana cara restart dengan aman (minim downtime)?

---

## Level: Middle

### Soal M1 - DNS & Networking triage
**Skenario:**
Sebuah host tidak bisa mengakses `api.internal.company`.

Output:
```text
$ curl -sS https://api.internal.company/health
curl: (6) Could not resolve host: api.internal.company

$ cat /etc/resolv.conf
nameserver 127.0.0.53
options edns0 trust-ad
search corp.local

$ resolvectl status | sed -n '1,80p'
Global
       LLMNR setting: yes
MulticastDNS setting: no
  DNSOverTLS setting: no
      DNSSEC setting: yes
    DNSSEC supported: yes
  Current DNS Server: 10.10.0.2
         DNS Servers: 10.10.0.2
          DNS Domain: corp.local
```

**Tugas:**
- Berikan triage dari layer paling dekat (local) sampai upstream DNS.
- Berikan minimal 6 perintah (kombinasi `resolvectl`, `dig`, `ip`, `ss`, `journalctl`) dan apa yang Anda harapkan dari outputnya.
- Berikan mitigasi cepat jika DNS server upstream bermasalah (tanpa mematikan security sepenuhnya).

### Soal M2 - CPU spike & process investigation
**Skenario:**
Load tinggi dan CPU 100% setelah deploy.

Output:
```text
$ uptime
 10:20:01 up 12 days,  3:02,  2 users,  load average: 12.40, 11.80, 9.22

$ ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head
  PID  PPID CMD                         %CPU %MEM
 8421  8310 /usr/bin/python3 worker.py  390  1.2
 8425  8310 /usr/bin/python3 worker.py  370  1.1
 8429  8310 /usr/bin/python3 worker.py  360  1.1
```

**Tugas:**
- Jelaskan kemungkinan penyebab `%CPU` > 100 pada output `ps`.
- Tunjukkan cara cepat menentukan apakah ini CPU-bound atau akibat thread/process explosion.
- Berikan langkah mitigasi cepat (throttle/rollback/limit) dan langkah perbaikan permanen.

### Soal M3 - Filesystem & inode exhaustion
**Skenario:**
`df -h` masih longgar, tapi aplikasi gagal membuat file.

Output:
```text
$ df -h /var
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G   18G   20G  48% /

$ df -i /var
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1       262144 262144       0  100% /
```

**Tugas:**
- Jelaskan perbedaan disk space vs inode.
- Tunjukkan langkah menemukan folder dengan jumlah file sangat banyak.
- Berikan perbaikan jangka pendek dan jangka panjang.

---

## Level: Senior

### Soal S1 - Incident: Latency spike (I/O + kernel)
**Skenario:**
API latency P99 naik dari 120ms ke 4-8s. CPU normal. Terjadi setiap 10-15 menit selama 1-2 menit.

Cuplikan data:
```text
$ vmstat 1 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 2  0      0 120000  90000 800000    0    0    30    50  400  600 10  5 85  0  0
 1  8      0 118000  85000 790000    0    0   120  9000 1200 3000  5  3 35 57  0

$ dmesg | tail -n 5
[123456.12] blk_update_request: I/O error, dev nvme0n1, sector 12345678
[123456.13] Buffer I/O error on dev nvme0n1p1, logical block 1543209
```

**Tugas:**
- Buat runbook 15 menit pertama: apa yang Anda cek, apa yang Anda kumpulkan, apa yang Anda komunikasikan.
- Bedakan mitigasi cepat vs diagnosis mendalam.
- Sertakan langkah untuk membuktikan apakah akar masalahnya storage device, filesystem, atau aplikasi.
- Sertakan rencana rollback/traffic-shift bila ini instance tunggal di fleet.

### Soal S2 - SSH access regression (hardening vs operability)
**Skenario:**
Setelah hardening, tim on-call tidak bisa SSH:

Output:
```text
$ ssh oncall@server
oncall@server: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).

$ sudo tail -n 5 /var/log/auth.log
sshd[2201]: userauth_pubkey: key type ssh-ed25519 not in PubkeyAcceptedKeyTypes [preauth]
sshd[2201]: Connection closed by authenticating user oncall 10.0.0.12 port 51122 [preauth]
```

**Tugas:**
- Jelaskan apa yang terjadi dan kenapa.
- Berikan solusi yang tetap secure (bukan sekadar "enable semuanya").
- Berikan rencana rollout hardening yang meminimalkan lockout (termasuk validasi sebelum apply).

### Soal S3 - Backup/restore verification (disaster readiness)
**Skenario:**
Anda menemukan bahwa backup database berjalan setiap malam, tapi belum pernah diuji restore. Anda harus membuktikan "backup bisa direstore" tanpa mengganggu production.

**Tugas:**
- Buat rencana verifikasi restore end-to-end.
- Sertakan isolasi lingkungan, sanitasi data (bila perlu), dan kriteria sukses.
- Sertakan contoh skrip/command high-level (mis. membuat environment sementara, restore, menjalankan smoke test).

---

## Penutup

Jika Anda merasa butuh info tambahan, tuliskan "Asumsi" secara eksplisit dan lanjutkan dengan pendekatan paling aman.
