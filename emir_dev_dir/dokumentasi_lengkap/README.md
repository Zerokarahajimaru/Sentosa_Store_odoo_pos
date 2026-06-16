# Dokumentasi Lengkap Modifikasi Odoo 19
**Proyek:** Toko Utama Sentosa

Dokumentasi ini disusun untuk memberikan pemahaman menyeluruh mengenai seluruh perubahan yang telah dilakukan pada sistem Odoo 19, baik dari sisi fungsional (logika) maupun visual (desain).

## Daftar Isi Dokumen:

1.  **[Bagian 1: Struktur Folder dan Arsitektur Modul](./01_Struktur_Folder.md)**
    *   Penjelasan hirarki folder modul `toko_utama_sentosa_custom`.
    *   Pembagian tanggung jawab antara Backend (Python) dan Frontend (JS/XML).

2.  **[Bagian 2: Penjelasan Fitur, File, dan Trigger (Pemicu)](./02_Penjelasan_File_dan_Trigger.md)**
    *   Detail setiap fitur (Notifikasi, Validasi Stok, Refund, Unbundling).
    *   Penjelasan teknis pemicu (*trigger*) berjalannya kode JavaScript.

3.  **[Bagian 3: Detail Perubahan Komponen UI & Desain](./03_Detail_Komponen_UI.md)**
    *   Bedah desain Premium Theme (Navy/Orange).
    *   Daftar komponen XML yang dimodifikasi.

---
**Catatan Penting:**
Seluruh file modifikasi berada di dalam direktori `/home/yukannahinoishi/odoo_19_fix/odoo19/custom_addons/toko_utama_sentosa_custom/`. Modul ini sudah siap di-deploy ke cloud (Render.com) menggunakan Docker.
