# Struktur Folder, File, dan Penjelasan Logika Modifikasi Odoo 19
**Studi Kasus:** Toko Utama Sentosa (Modul: `toko_utama_sentosa_custom`)

Dokumen ini menjelaskan arsitektur kode dari modul kustom yang telah dibuat, file apa saja yang diubah/ditambahkan, serta penjelasan *trigger* (pemicu) dari aksi-aksi sistem.

---

## 1. Arsitektur Folder (Folder Structure)
Seluruh modifikasi kode kita diisolasi dalam satu *custom module* agar tidak merusak kode inti (core) Odoo. Modul tersebut berada di:
`custom_addons/toko_utama_sentosa_custom/`

Berikut adalah struktur hirarkinya:
```text
toko_utama_sentosa_custom/
│
├── __init__.py                # Inisialisasi modul Python
├── __manifest__.py            # Jantung modul: Mendefinisikan nama, versi, dan mendaftarkan semua aset (XML, JS, SCSS) ke sistem Odoo.
│
├── models/                    # BACKEND: Logika Bisnis & Database (Python)
│   ├── __init__.py            
│   ├── pos_order.py           # Menambah kolom jadwal kirim & alasan refund ke DB
│   ├── product_template.py    # Menambah kolom dimensi, material, & logika pecah paket (bundle)
│   └── stock_picking.py       # Menghubungkan pesanan POS dengan surat jalan
│
└── static/                    # FRONTEND: Tampilan & Interaksi Kasir (JS, SCSS, XML)
    └── src/
        ├── js/                # Logika Interaksi Web Kasir (Frontend Odoo/OWL)
        │   ├── pos_notifications.js    # Trigger notifikasi kemasan khusus
        │   ├── pos_refund_reason.js    # Trigger pop-up alasan refund
        │   └── pos_stock_validation.js # Validasi stok fisik dan jadwal kirim sebelum bayar
        │
        ├── scss/              # Desain Visual (Warna & Tata Letak)
        │   ├── pos_ui.scss             # Mengubah warna tema kasir menjadi High-Contrast Navy/Orange
        │   ├── pos_login.scss          # Modifikasi halaman login
        │   └── backend_dashboard.scss  # Modifikasi dashboard admin
        │
        └── xml/               # Kerangka/Layout Elemen Layar Kasir
            ├── pos_delivery_schedule.xml # Menambahkan input jadwal di layar pembayaran
            ├── pos_product_info.xml      # Menampilkan dimensi & material di bawah nama produk
            └── pos_refund_reason.xml     # Desain kotak pop-up alasan refund
```

---

## 2. Penjelasan Perubahan File & Pemicu (Triggers)

Berikut adalah penjelasan detail mengapa suatu file diubah dan apa yang memicu berjalannya kode tersebut.

### A. Fitur Notifikasi Peringatan Kemasan Khusus
*   **File yang dimodifikasi:** `static/src/js/pos_notifications.js`
*   **Apa yang diubah:** Melakukan *Monkey Patching* (menimpa fungsi bawaan) pada metode `addLineToCurrentOrder` milik `ProductScreen`.
*   **Trigger (Pemicu):** Kode ini terpicu **setiap kali kasir mengklik gambar produk** atau **melakukan scan barcode**.
*   **Logika:** 
    1. Kasir klik produk.
    2. Sistem mencegat (intercept) perintah masuk keranjang.
    3. Sistem mengecek *Kategori Produk* (`product.pos_categ_ids`).
    4. **Kondisi:** Jika nama kategori mengandung kata "Alat potong", "Bahan kimia", "Cairan", atau "Senjata", maka sistem akan memanggil komponen dialog (`AlertDialog`).
    5. Pop-up peringatan warna merah bata (Terracotta) muncul.

### B. Fitur Validasi Stok & Jadwal Kirim
*   **File yang dimodifikasi:** `static/src/js/pos_stock_validation.js`
*   **Apa yang diubah:** Mem-patch metode `validateOrder` pada `PaymentScreen`.
*   **Trigger (Pemicu):** Kode ini terpicu ketika kasir menekan **Tombol Validasi (Validate)** di layar pembayaran.
*   **Logika:**
    1. Sebelum Odoo memproses pembayaran, script kita menahannya.
    2. Mengambil data dari inputan XML (Jadwal Kirim & Centang Mobil Pickup) lalu menyimpannya ke objek `order`.
    3. Mengambil daftar belanjaan, lalu melakukan *Remote Procedure Call (RPC)* ke backend Python (`check_stock_availability`).
    4. **Kondisi:** Jika backend menjawab "stok fisik < 0", maka proses pembayaran dibatalkan (return false) dan muncul pop-up error. Jika aman, lanjut ke `super.validateOrder()` (pembayaran sukses).

### C. Fitur Alasan Refund (Retur) Wajib
*   **File JS:** `static/src/js/pos_refund_reason.js` (Mem-patch tombol klik bayar jika statusnya retur).
*   **File XML:** `static/src/xml/pos_refund_reason.xml` (Kerangka pop-up pilihan alasan).
*   **File Python:** `models/pos_order.py` (Menyimpan alasan ke database).
*   **Trigger (Pemicu):** Terpicu saat kasir menekan tombol **Refund** dan akan melakukan pembayaran (dengan nominal minus).
*   **Logika:**
    Jika nominal pesanan bernilai negatif (artinya retur), sistem akan memblokir aksi validasi dan memunculkan pop-up yang memaksa kasir memilih alasan (Cacat Pabrik, Tidak Muat, dll) sebelum uang bisa dikembalikan.

### D. Fitur Tampilan Dimensi & Material Realtime
*   **File XML:** `static/src/xml/pos_product_info.xml`
*   **Apa yang diubah:** Melakukan ekstensi (t-inherit) pada kerangka `point_of_sale.Orderline` (daftar belanja) dan `point_of_sale.OrderReceipt` (struk belanja).
*   **Trigger (Pemicu):** Terpicu secara pasif (otomatis) saat layar kasir merender (menggambar) daftar barang di sebelah kiri layar atau saat mencetak struk.
*   **Logika:** 
    Sistem mengecek data produk. Jika field `custom_dimension` atau `custom_material` di database terisi, maka elemen `<span>` berisi informasi tersebut (dengan icon penggaris/kubus) akan disisipkan tepat di bawah nama produk.

### E. Fitur Pecah Paket (Bundle Breaker)
*   **File Python:** `models/product_template.py`
*   **Apa yang diubah:** Menambahkan fungsi Python murni (Backend).
*   **Trigger (Pemicu):** Terpicu saat Admin Gudang mengklik tombol **"Pecah Paket"** di halaman master data produk (Backend).
*   **Logika:**
    Tombol tersebut memanggil fungsi Python yang secara transaksional: mengurangi 1 unit stok produk induk (misal: "Set Meja Makan") dan menambah jumlah unit produk anak (misal: "Kursi Satuan") sebanyak nilai `bundle_qty` yang disetting.
