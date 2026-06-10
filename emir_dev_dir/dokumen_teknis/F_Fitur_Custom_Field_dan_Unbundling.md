# Dokumentasi Fitur: Custom Field Material, Dimensi, & Unbundling (Pecah Paket)

## 1. Skenario Penggunaan
Toko sering menerima barang dalam bentuk "Paketan/Grosir" (contoh: Set Piring isi 12) yang kadang perlu dipecah untuk dijual satuan. Staf gudang butuh satu tombol khusus yang dapat mengurangi stok paket dan menambah stok satuan tanpa input manual yang rumit. Selain itu, staf butuh mencatat Dimensi dan Material barang.

## 2. Lokasi Fitur
- **Backend Inventory - Master Data Produk** (`product.template` & `product.product`).

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Pegawai gudang harus membuat Inventory Adjustment manual untuk mengurangi barang set dan menambah barang satuan secara terpisah. Tidak ada kolom Dimensi dan Material pada produk.
- **SESUDAH:** Terdapat tombol **"Pecah Paket (Unbundle)"** di menu produk. Saat ditekan, stok barang tersebut berkurang 1 dan otomatis stok barang "Item Satuan" bertambah sesuai konfigurasi (misal +12). Terdapat juga tab "Informasi Spesifik Sentosa" untuk mengisi dimensi dan material.

## 4. Perubahan Skema Database
Model: `product.template` & `product.product`
- **Kolom Baru Ditambahkan:**
  - `custom_dimensions` (Type: `VARCHAR/Char`)
  - `custom_material` (Type: `VARCHAR/Char`)
  - `is_bundle` (Type: `Boolean`)
  - `bundle_item_id` (Type: `Many2one` ke `product.product`)
  - `bundle_qty` (Type: `Integer`)
