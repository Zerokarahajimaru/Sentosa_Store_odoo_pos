# Bagian 2: Penjelasan Fitur, File, dan Trigger (Pemicu)
**Toko Utama Sentosa - Odoo 19 Customization**

Di bagian ini, kita akan membedah setiap fitur kustom, file mana yang bertanggung jawab, dan apa yang membuat fitur tersebut berjalan (Trigger).

---

## 1. Fitur: Peringatan Kemasan Khusus
*   **Tujuan:** Memberi peringatan ke kasir jika ada barang berbahaya (tajam/kimia) agar dikemas dengan aman.
*   **File yang Bertanggung Jawab:** `static/src/js/pos_notifications.js`
*   **Trigger (Pemicu):** Fungsi `addLineToCurrentOrder` pada `ProductScreen`.
*   **Cara Kerja:** 
    Setiap kali kasir **klik produk** atau **scan barcode**, JavaScript akan langsung mengecek kategori produk tersebut. Jika nama kategori mengandung kata kunci "Alat potong", "Senjata", atau "Bahan Kimia", maka sistem akan membatalkan input sesaat untuk memunculkan pop-up `AlertDialog` (Peringatan).

## 2. Fitur: Validasi Stok Fisik & Jadwal Kirim
*   **Tujuan:** Memastikan stok di gudang benar-benar ada sebelum dibayar dan mencatat jadwal pengiriman mobil pickup.
*   **File yang Bertanggung Jawab:** 
    *   `static/src/js/pos_stock_validation.js` (Logika)
    *   `static/src/xml/pos_delivery_schedule.xml` (Tampilan Input)
*   **Trigger (Pemicu):** Klik tombol **Validate (Bayar)** pada `PaymentScreen`.
*   **Cara Kerja:**
    Saat kasir menekan tombol bayar, sistem tidak langsung memproses pembayaran. JavaScript akan:
    1.  Membaca nilai dari input `custom_delivery_date` di XML.
    2.  Melakukan **RPC Call** (panggilan jarak jauh) ke server untuk bertanya: *"Server, apakah stok barang-barang di keranjang ini mencukupi?"*.
    3.  Jika server menjawab stok kurang, proses bayar dihentikan. Jika cukup, proses dilanjutkan.

## 3. Fitur: Alasan Refund Wajib
*   **Tujuan:** Kasir wajib memilih alasan (misal: "Barang Cacat") saat melakukan retur uang.
*   **File yang Bertanggung Jawab:**
    *   `static/src/js/pos_refund_reason.js` (Pop-up pemicu)
    *   `static/src/xml/pos_refund_reason.xml` (Desain Pop-up)
*   **Trigger (Pemicu):** Mendeteksi nilai pesanan **Negatif** saat tombol bayar diklik.
*   **Cara Kerja:**
    Sistem mengecek total belanja. Jika totalnya minus (retur), maka JavaScript akan memunculkan komponen `RefundReasonPopup`. Kasir tidak bisa melanjutkan pembayaran sampai salah satu alasan dipilih.

## 4. Fitur: Pecah Paket (Unbundling)
*   **Tujuan:** Memecah 1 set furnitur menjadi beberapa bagian satuan secara otomatis di inventory.
*   **File yang Bertanggung Jawab:** `models/product_template.py` (Python/Backend).
*   **Trigger (Pemicu):** Klik tombol **"Pecah Paket"** di form produk (Backend).
*   **Cara Kerja:**
    Tombol ini memicu fungsi Python `action_unbundle`. Fungsi ini secara transaksional mengurangi stok produk induk sebanyak 1, dan menambah stok produk komponen (anak) sebanyak jumlah yang sudah ditentukan di field `bundle_qty`.

## 5. Fitur: Informasi Dimensi & Material Real-time
*   **Tujuan:** Menampilkan spek barang (P x L x T) langsung di layar kasir dan struk.
*   **File yang Bertanggung Jawab:** `static/src/xml/pos_product_info.xml`
*   **Trigger (Pemicu):** Proses *Rendering* komponen `Orderline`.
*   **Cara Kerja:**
    Setiap kali layar kasir menggambar daftar belanjaan, XML kita yang sudah mem-*patch* elemen `product-name` akan otomatis menyisipkan icon penggaris dan teks dimensi di bawah nama produk tersebut jika datanya tersedia di database.
