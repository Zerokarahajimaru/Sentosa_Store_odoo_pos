# Bagian 3: Detail Perubahan Komponen UI & Desain
**Toko Utama Sentosa - Odoo 19 Premium Theme**

Bagian ini menjelaskan file mana yang mengubah elemen visual spesifik pada layar kasir (Theme customization).

---

## 1. Tema Warna Premium (Navy & Orange)
*   **File:** `static/src/scss/pos_ui.scss`
*   **Perubahan Utama:**
    *   **Header & Sidebar:** Diubah menjadi warna Navy Blue (`#003366`) agar terlihat profesional.
    *   **Tombol Aksi (Action Pad):** Tombol "Bayar" (Payment) diubah menjadi warna Cobalt Blue dengan bayangan (*floating shadow*), memberikan kesan modern.
    *   **Peringatan (Alerts):** Seluruh elemen peringatan diubah menggunakan aksen warna Cadmium Orange (`#FF9912`) dan Terracotta.
    *   **Kelengkungan (Border Radius):** Semua kotak diubah dari siku-siku menjadi melengkung halus (12px - 24px) untuk kesan UI kekinian.

## 2. Modifikasi Footer & Area Tombol
*   **File:** `static/src/xml/pos_delivery_schedule.xml`
*   **Detail:** 
    Kita melakukan *inheritance* ke template `point_of_sale.PaymentScreenButtons`. 
    *   **Apa yang dilakukan?** Kita menyisipkan satu blok div baru tepat **SEBELUM** tombol-tombol angka. 
    *   **Hasil:** Di layar pembayaran, muncul kotak putih rapi berisi input tanggal dan checkbox mobil pickup.

## 3. Halaman Login Kustom
*   **File:** `static/src/scss/pos_login.scss`
*   **Detail:** 
    Mengubah halaman pemilihan kasir (Login) agar tidak menggunakan gaya standar Odoo. Kita menambahkan latar belakang yang lebih bersih dan tombol user yang lebih besar serta responsif.

## 4. Dashboard Backend (Admin)
*   **File:** `static/src/scss/backend_dashboard.scss`
*   **Detail:** 
    Mengubah gaya tombol "Pecah Paket" di menu Inventory agar berwarna hijau daun, memudahkan admin gudang mengenali tombol fungsi khusus tersebut di tengah banyaknya tombol standar Odoo.

## 5. Tampilan Baris Produk (Orderline)
*   **File:** `static/src/xml/pos_product_info.xml`
*   **Detail:** 
    Menambahkan kelas CSS kustom `.product-info-custom` pada elips di bawah nama produk. Ini diatur menggunakan Flexbox agar icon dan teks dimensi sejajar rapi.
