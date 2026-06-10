# Dokumentasi Fitur: Penjadwalan Pengiriman & Pickup

## 1. Skenario Penggunaan
Toko Utama Sentosa memiliki layanan pengiriman mandiri menggunakan mobil pickup toko untuk barang besar. Saat pelanggan membeli barang berukuran besar di kasir, kasir perlu menginput jadwal tanggal pengiriman dan apakah barang dikirim menggunakan layanan mobil pickup khusus toko. Data ini akan diteruskan ke tim gudang (Delivery Order).

## 2. Lokasi Fitur
- **Layar Payment Screen PoS** (Frontend OWL, di samping tombol validasi pembayaran).
- **Backend PoS Order & Transfer/Delivery Order (Stock Picking)**.

## 3. Behaviour SEBELUM vs SESUDAH
- **SEBELUM:** Tidak ada form input tanggal pengiriman dan checkbox pickup di layar kasir. Order langsung tervalidasi dan DO (Delivery Order) tidak memiliki penanda khusus.
- **SESUDAH:** Layar pembayaran kini memiliki komponen kalender (*Date/Time Picker*) dan checkbox "*Kirim via Mobil Pickup Khusus*". Setelah order divalidasi, data ini tersimpan di tiket pesanan dan muncul di form Delivery Order (Inventory).

## 4. Perubahan Skema Database
Model: `pos.order` (Tabel: `pos_order`) dan `stock.picking` (Tabel: `stock_picking`)
- **Kolom Baru Ditambahkan:**
  - `custom_delivery_date` (Type: `Datetime`)
  - `custom_is_pickup` (Type: `Boolean/Checkbox`)
