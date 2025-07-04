import sys
import os
import shutil

# Nama file .so
filename = "retas.cpython-312.so"

# Lokasi target site-packages
dst = f"/data/data/com.termux/files/usr/lib/python3.12/site-packages/{filename}"

# Cek kalau sudah ada
if not os.path.exists(dst):
    print("[*] Mencari modul...")
    found = False
    # Cari mulai dari lokasi script ini
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            src = os.path.join(root, filename)
            print(f"[*] Ditemukan di: {src}")
            print("[*] Memindahkan modul ke site-packages...")
            shutil.move(src, dst)
            found = True
            break

    if not found:
        print("[!] File .so tidak ditemukan. Pastikan file ada di dalam folder project.")
        sys.exit(1)
else:
    print("[*] Modul sudah tersedia di site-packages.")

# Pastikan site-packages masuk sys.path
sys.path.append("/data/data/com.termux/files/usr/lib/python3.12/site-packages/")

# Import modul
import retas

# Jalankan fungsi main()
retas.main()