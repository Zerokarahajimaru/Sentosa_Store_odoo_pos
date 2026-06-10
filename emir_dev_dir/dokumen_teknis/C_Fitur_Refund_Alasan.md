# Dokumentasi Fitur: Alasan Refund Barang Cacat

## 1. Skenario Penggunaan
Toko sering menerima retur barang. Untuk keperluan pelaporan dan audit, manajer toko ingin agar setiap kasir yang menekan tombol "Refund" wajib menginputkan alasan pengembalian (misalnya barang cacat pabrik atau rusak pengiriman).

## 2. Lokasi Fitur
- **Layar Ticket Screen PoS** (Frontend OWL, saat menekan tombol `Refund` pada tiket transaksi sebelumnya).
- **Backend PoS Order** (`/odoo/point-of-sale/orders`).

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Saat kasir menekan tombol "Refund" di menu Order/Ticket, sistem langsung membuat order minus baru tanpa menanyakan alasan.
- **SESUDAH:** Saat kasir menekan "Refund", sistem menahan proses dan memunculkan **Pop-up Dropdown** berisi daftar alasan (misal: Barang Cacat Pabrik, Rusak Pengiriman, dll). Alasan yang dipilih akan disematkan ke dalam Order PoS tersebut.

## 4. Perubahan Skema Database
Model: `pos.order` (Tabel Database: `pos_order`)
- **Kolom Baru Ditambahkan:** `refund_reason` (Type: `VARCHAR/Char`)
