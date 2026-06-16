# Jawaban Pertanyaan Teknis (FAQ) - Toko Utama Sentosa
**Dokumen Persiapan Sidang/Presentasi**

Berikut adalah jawaban atas pertanyaan abang (tanda ???? pada ringkasan) disertai dengan referensi kode dan justifikasi teknisnya.

---

### 1. Kenapa notifikasi "Kuantitas < 0" baru muncul setelah klik Payment?
**Jawaban:**
Secara teknis, pengecekan stok fisik dilakukan pada saat **Validasi Final** (saat menekan tombol bayar) untuk menjamin akurasi data yang paling *real-time*.

*   **Justifikasi:** Dalam lingkungan POS, beberapa kasir bisa menjual barang yang sama secara bersamaan. Jika pengecekan dilakukan saat barang masuk keranjang, ada risiko "Race Condition" (stok terlihat ada saat discan, tapi sebenarnya sudah habis dibayar oleh kasir lain semenit kemudian). Dengan mengecek tepat sebelum transaksi sah (saat klik Payment), sistem memastikan stok benar-benar ada di gudang sebelum uang diterima.
*   **Referensi Kode:** 
    *   **File:** `static/src/js/pos_stock_validation.js`
    *   **Baris:** Metode `async validateOrder(isForceValidate)`.
    *   **Logika:** Kode memanggil `this.pos.data.orm.call('pos.order', 'check_stock_availability', ...)` yang merupakan gerbang terakhir sebelum data masuk ke database.

---

### 2. Apakah notifikasi "Peringatan Kemasan" hanya untuk benda tajam saja?
**Jawaban:**
**Tidak.** Saat ini sistem sudah mencakup 4 kategori besar barang berbahaya/sensitif, bukan hanya benda tajam.

*   **Daftar Kategori Saat Ini:**
    1.  **Alat potong** (Pisau, gergaji, dll)
    2.  **Bahan kimia** (Pembersih lantai keras, tiner, dll)
    3.  **Cairan yang mudah terbakar** (Alkohol, spiritus)
    4.  **Senjata tajam** (Golok, dll)
*   **Justifikasi:** Toko furniture/bangunan seperti Utama Sentosa sering menjual bahan kimia (tiner/cat) dan alat pertukangan tajam yang butuh penanganan logistik khusus agar tidak merusak barang lain di mobil pengiriman.
*   **Referensi Kode:** 
    *   **File:** `static/src/js/pos_notifications.js`
    *   **Logika:** Mencari kata kunci (keywords) menggunakan regex: `/alat potong|bahan kimia|cairan yang mudah terbakar|senjata tajam/i`.

---

### 3. Bagaimana cara menambah kategori agar mendapatkan notifikasi tersebut?
**Jawaban:**
Ada dua cara, abang bisa pilih salah satu:

**Cara A (Tanpa Koding - Rekomendasi):**
Abang cukup pastikan **Nama Kategori POS** di backend Odoo mengandung salah satu kata kunci di atas. 
*   *Contoh:* Buat kategori baru bernama "Aksesoris - Bahan Kimia". Semua produk di dalamnya otomatis akan memicu notifikasi.

**Cara B (Lewat Kode):**
Abang bisa menambah kata kunci baru di dalam script JavaScript.
1.  Buka file `static/src/js/pos_notifications.js`.
2.  Cari bagian `const dangerousKeywords`.
3.  Tambahkan kata kunci baru di sana (misal: "Barang Pecah Belah").
*   **Referensi Kode:** 
    ```javascript
    const dangerousKeywords = /alat potong|bahan kimia|cairan yang mudah terbakar|senjata tajam|barang pecah belah/i;
    ```

---

### 4. Fitur apa yang terlewat (Belum disebutkan abang)?
Berdasarkan pengerjaan saya, ada **2 Fitur Penting** yang belum abang masukkan di ringkasan:

1.  **Jadwal Pengiriman Mobil Pickup:**
    *   **Kegunaan:** Kasir bisa mencatat tanggal dan jam pasti kapan barang harus dikirim menggunakan armada toko.
    *   **File:** `static/src/xml/pos_delivery_schedule.xml` dan `models/pos_order.py`.
2.  **Logika Pecah Paket (Unbundling):**
    *   **Kegunaan:** Fitur untuk memecah stok paket (misal: 1 Set Meja) menjadi stok satuan (4 Kursi) hanya dengan satu klik tombol di master produk.
    *   **File:** `models/product_template.py`.

---

Dokumen ini disusun untuk memperkuat argumen abang saat ditanya dosen mengenai efisiensi dan keamanan data sistem yang dibangun. 🚀✨
