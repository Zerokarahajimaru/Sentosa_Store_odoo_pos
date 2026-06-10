# Dokumentasi Fitur: Notifikasi Pengemasan Khusus

## 1. Skenario Penggunaan
Saat kasir memindai (scan) atau mengklik produk di layar PoS yang memiliki kategori berbahaya (seperti "Alat potong", "Bahan kimia", "Cairan yang mudah terbakar", atau "Senjata tajam"), sistem akan menampilkan pop-up peringatan agar kasir tahu barang tersebut perlu penanganan atau pengemasan khusus (misal: diplastik ganda, ditaruh di wadah aman).

## 2. Lokasi Fitur
- **Halaman Utama Layar Kasir PoS** (Frontend OWL, saat aksi tambah produk ke keranjang).

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Kasir memindai barang tajam atau kimia, barang langsung masuk keranjang tanpa ada peringatan apa pun.
- **SESUDAH:** Sistem mencegat (intercept) penambahan barang. Jika kategori produk mengandung kata kunci berbahaya, muncul **Pop-up Dialog Peringatan** di layar kasir. Setelah kasir menekan "OK", barang baru ditambahkan ke keranjang.

## 4. Perubahan Skema Database
- *Tidak ada kolom baru. Membaca data relasi kategori bawaan (`pos_categ_ids`) dari model produk.*
