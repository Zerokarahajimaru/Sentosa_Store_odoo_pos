# Dokumentasi Fitur: Validasi Blokir Stok Kosong

## 1. Skenario Penggunaan
Banyak terjadi selisih stok (minus) karena kasir tetap bisa menjual barang yang secara fisik di sistem sedang kosong. Manajemen toko mewajibkan pemblokiran transaksi di kasir (PoS) jika stok barang di gudang Odoo ternyata kurang dari 0.

## 2. Lokasi Fitur
- **Layar Payment Screen PoS** (Frontend OWL, fungsi validasi pembayaran).
- **Backend PoS Order** (Method RPC `check_stock_availability`).

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Transaksi akan tembus tanpa peduli apakah stok barang tersebut ada di gudang atau sudah minus, asalkan produk tersebut dapat dijual di PoS.
- **SESUDAH:** Sesaat sebelum pembayaran divalidasi, sistem PoS akan melakukan panggilan ke backend (RPC Call) untuk mengecek ketersediaan fisik stok produk. Jika ada barang yang kosong atau minus, transaksi akan otomatis **DIBLOKIR** dan layar memunculkan peringatan pop-up "Stok Kosong". (Catatan Edge Case: Jika internet kasir mati, sistem memberikan kelonggaran agar kasir tidak terblokir karena gagal RPC).

## 4. Perubahan Skema Database
- *Tidak ada kolom baru. Hanya penambahan method Python/RPC.*
