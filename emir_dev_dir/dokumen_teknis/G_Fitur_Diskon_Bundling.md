# Dokumentasi Fitur: Diskon Bundling Otomatis

## 1. Skenario Penggunaan
Toko Utama Sentosa memiliki promosi: Jika pelanggan membeli barang "Meja" dan "Kursi" secara bersamaan dalam satu struk transaksi, mereka otomatis mendapatkan diskon bundling 10% untuk barang tersebut.

## 2. Lokasi Fitur
- **Backend PoS Order** (Metode Python `_process_order`).

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Kasir harus mengingat promo dan menekan tombol diskon secara manual untuk masing-masing item di keranjang belanja.
- **SESUDAH:** Skrip Python di backend secara pintar membaca dan mengevaluasi keranjang belanja sesaat sebelum order tersimpan di database. Jika terdapat minimal satu barang dengan nama "Meja" dan satu barang dengan nama "Kursi", sistem akan otomatis mem-patch (mengaplikasikan) diskon minimal sebesar 10% pada baris-baris pesanan tersebut secara backend, sehingga omzet tercatat rapi dengan promo diskon.

## 4. Perubahan Skema Database
- *Tidak ada kolom baru. Modifikasi logika perhitungan harga/diskon di method ORM.*
