# Toko Utama Sentosa Custom POS - Odoo 19

Modul kustomisasi Point of Sale (POS) untuk Toko Utama Sentosa, mencakup fitur peringatan kemasan khusus, penjadwalan pengiriman, manajemen stok, dan UI/UX premium.

## 🚀 Panduan Setup Pengembangan

Ikuti langkah-langkah di bawah ini untuk menjalankan project ini di mesin lokal Anda.

### 1. Prasyarat
* Odoo 19 Community/Enterprise source code.
* PostgreSQL 16+.
* Python 3.12+.

### 2. Setup Database
Pastikan Anda sudah membuat database di PostgreSQL (misal: `odoo_polban_19`). Untuk melakukan restore database dari backup yang disediakan:

1. Buka terminal.
2. Masuk ke direktori backup:
   ```bash
   cd   ./emir_dev_dir/backup_db
   ```
3. Jalankan perintah restore:
   ```bash
   psql -U postgres [NAMA_DATABASE_ANDA] < finalize_db.sql
   ```
   *(Catatan: Sesuaikan `[NAMA_DATABASE_ANDA]` dengan nama database yang Anda buat di PostgreSQL).*

### 3. Menjalankan Server Odoo
Gunakan perintah berikut untuk menjalankan server Odoo dengan mengaktifkan modul kustom `toko_utama_sentosa_custom`:

```bash
python odoo-bin --addons-path=addons,custom_addons -d [NAMA_DATABASE_ANDA] -u toko_utama_sentosa_custom
```

**Penjelasan Flag:**
* `--addons-path=addons,custom_addons`: Menentukan lokasi folder modul (modul bawaan Odoo dan modul kustom kita).
* `-d odoo_polban_19`: Menentukan database yang digunakan (sesuaikan dengan nama DB masing-masing).
* `-u toko_utama_sentosa_custom`: Melakukan update pada modul kustom agar perubahan kode (Python/XML/SCSS) diterapkan ke sistem.

### 4. Akses POS
Setelah server berjalan:
1. Buka browser dan akses `http://localhost:8069`.
2. Login dengan akun admin Anda.
3. Buka Dashboard **Point of Sale**.
4. Klik **New Session** atau **Continue** pada konfigurasi POS yang diinginkan.

---

## 🎨 Informasi UI/UX
Project ini menggunakan palet warna kustom:
* **Primary:** Navy Blue (#003366)
* **Action:** Cobalt Blue (#3d59AB)
* **Warning:** Cadmium Orange (#FF9912)
* **Success:** Teal (#03A89E)

Desain berbasis **Card-Based UI** dengan sudut membulat (20px) dan efek *floating shadow* untuk memberikan kesan premium.

---
*Dikembangkan oleh Tim Senior UI/UX & Frontend*
