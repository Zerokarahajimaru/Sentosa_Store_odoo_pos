# Rincian File Modifikasi Berdasarkan Fitur
**Toko Utama Sentosa - Odoo 19 Technical Breakdown**

Dokumen ini merinci file apa saja yang diubah atau ditambah untuk setiap fitur yang telah diimplementasikan.

---

## 1. Fitur: Alasan Refund (Retur) Wajib
*   **File JS:** `static/src/js/pos_refund_reason.js`
    *   **Penjelasan:** Menggunakan *Monkey Patching* pada metode `validateOrder`. Jika total pesanan negatif (refund), script akan memunculkan pop-up pilihan alasan.
*   **File XML:** `static/src/xml/pos_refund_reason.xml`
    *   **Penjelasan:** Kerangka tampilan dialog pop-up yang berisi daftar alasan (misal: "Barang Cacat", "Salah Ukuran").
*   **File Python:** `models/pos_order.py`
    *   **Penjelasan:** Menambah field `refund_reason` ke database agar data alasan yang dipilih kasir tersimpan permanen.

## 2. Fitur: Informasi Material & Volume (Dimensi)
*   **File XML:** `static/src/xml/pos_product_info.xml`
    *   **Penjelasan:** Melakukan *inheritance* pada `point_of_sale.Orderline`. Menambahkan elemen visual tepat di bawah nama produk untuk menampilkan spek teknis secara real-time di layar kasir dan struk.
*   **File Python:** `models/product_template.py`
    *   **Penjelasan:** Menambah kolom `custom_dimension` dan `custom_material` ke database master produk agar bisa diinput oleh admin gudang.

## 3. Fitur: Tema Warna Premium (Navy & Orange)
*   **File SCSS:** `static/src/scss/pos_ui.scss`
    *   **Penjelasan:** Mengganti skema warna standar Odoo. Menggunakan variabel `$primary-navy` untuk header/sidebar dan `$terracotta` untuk aksen peringatan. Menambahkan efek bayangan (*shadow*) pada kartu produk.

## 4. Fitur: Validasi Stok Fisik (< 0)
*   **File JS:** `static/src/js/pos_stock_validation.js`
    *   **Penjelasan:** Script ini mencegat proses pembayaran. Dia mengirimkan data keranjang ke server via RPC sebelum bayar disahkan. Jika server bilang stok gudang habis, JS akan memunculkan error dan memblokir transaksi.
*   **File Python:** `models/pos_order.py`
    *   **Penjelasan:** Menambahkan fungsi `@api.model check_stock_availability` yang bertugas menghitung sisa stok fisik di database PostgreSQL untuk merespon permintaan dari JavaScript.

## 5. Fitur: Notifikasi Pengemasan Barang Tajam/Kimia
*   **File JS:** `static/src/js/pos_notifications.js`
    *   **Penjelasan:** Memantau setiap produk yang masuk ke keranjang belanja. Menggunakan pencocokan string (*string matching*) pada kategori produk untuk mendeteksi barang sensitif dan langsung memicu pop-up peringatan kemasan khusus.

## 6. Fitur: Jadwal Pengiriman & Mobil Pickup
*   **File XML:** `static/src/xml/pos_delivery_schedule.xml`
    *   **Penjelasan:** Menambahkan input tipe `datetime-local` dan `checkbox` di layar pembayaran kasir.
*   **File Python:** `models/pos_order.py` & `models/stock_picking.py`
    *   **Penjelasan:** Menyimpan data jadwal kirim ke pesanan kasir dan otomatis menyalinnya ke Surat Jalan Gudang (Stock Picking) agar tim logistik tahu kapan harus berangkat.

## 7. Fitur: Pecah Paket (Unbundling)
*   **File Python:** `models/product_template.py`
    *   **Penjelasan:** Menambahkan tombol "Pecah Paket" di backend. Logikanya melakukan manipulasi stok otomatis (mengurangi stok paket besar, menambah stok barang eceran secara instan).
