# Dokumentasi Fitur: UI/UX & Frontend Styling

## 1. Skenario Penggunaan
Kasir toko menggunakan Point of Sale (PoS) setiap hari. Untuk meningkatkan kenyamanan mata dan sesuai dengan identitas perusahaan (Toko Utama Sentosa), antarmuka (UI/UX) diubah dengan warna-warna baru yang lebih adem dan profesional.

## 2. Lokasi Fitur
- **Halaman Utama Layar Kasir PoS** (Frontend OWL)
- **Halaman Login Session PoS** (Frontend OWL / Backend)
- **Dashboard Backend PoS** (`/odoo/point-of-sale`)

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Menggunakan tema default Odoo (warna dominan putih, ungu Odoo, abu-abu standar). Tombol-tombol kurang menonjol dan dashboard backend terlihat bawaan.
- **SESUDAH:** 
  - Header PoS berubah menjadi **Biru Navy (#003366)**.
  - Background area produk menggunakan warna **Krem Hangat (#FAF0E6)**.
  - Tombol aksi kritis seperti "Refund" memiliki aksen **Terracotta (#E2725B)**.
  - Tombol validasi pembayaran memiliki aksen **Hijau (#A4D65E)**.
  - Dashboard PoS dan halaman login PoS disesuaikan dengan palet warna yang sama (border biru navy, shadow halus).

## 4. Perubahan Skema Database
- *Tidak ada penambahan kolom/tabel baru untuk fitur ini. Sepenuhnya modifikasi SCSS (CSS).*
