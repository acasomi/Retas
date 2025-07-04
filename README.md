# 🔓 Retas
TOOLS INI UNTUK MERETAS KEY / LICENSE TOOLS YANG MEMBUTUHKAN LICENSI

---

## 📘 Deskripsi
**Retas** adalah skrip otomatis yang digunakan untuk bypass script yang dikunci key atau license.  
Alat ini dibuat untuk mempermudah audit keamanan terhadap script yang dikunci lisensi (*license locked*).

---

## ⚙️ Fitur Utama
✅ Pencarian otomatis file dengan kata kunci:
- `vip`
- `sandi`
- `key`
- `license`
- `id`

✅ Sistem startup (berjalan sekali) untuk:
- Menginstal modul Python yang diperlukan (`requests`).
- Membuat backup otomatis skrip.

---

## 🛠️ Instalasi

### 📱 Termux
Salin dan tempel perintah berikut di Termux:

```bash
pkg update && pkg upgrade
pkg install python
pkg install git
pip install requests
git clone https://github.com/acasomi/Retas.git
cd Retas
python run.py
