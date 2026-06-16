# Bagian 1: Struktur Folder dan Arsitektur Modul
**Toko Utama Sentosa - Odoo 19 Customization**

Modul kustom kita bernama `toko_utama_sentosa_custom`. Modul ini dirancang agar terpisah sepenuhnya dari kode standar Odoo, sehingga aman saat ada pembaharuan sistem.

## Hirarki Direktori
```text
toko_utama_sentosa_custom/
├── __init__.py                 # Mengimpor folder 'models' agar Python mengenali modul database.
├── __manifest__.py             # 'KTP' Modul: Berisi daftar semua file XML, JS, dan CSS yang harus dimuat oleh Odoo.
│
├── models/                     # [BACKEND] Folder khusus untuk urusan Database dan Tabel.
│   ├── __init__.py             # Mengimpor semua file Python di folder ini.
│   ├── pos_order.py            # Modifikasi tabel Pesanan POS (tambah kolom alasan refund, dll).
│   ├── product_template.py     # Modifikasi tabel Produk (tambah kolom dimensi, material, & tombol pecah paket).
│   └── stock_picking.py        # Menghubungkan data POS ke sistem Gudang (Inventory).
│
├── static/                     # [FRONTEND] Folder khusus untuk tampilan dan interaksi web.
│   └── src/
│       ├── js/                 # Logika JavaScript (Cara kerja tombol, notifikasi, dan validasi).
│       ├── scss/               # Desain CSS/SCSS (Warna, bayangan, dan font premium).
│       └── xml/                # Kerangka XML (Posisi input, logo, dan penempatan informasi baru).
│
└── data/                       # [INITIAL DATA]
    └── cloud_migration_backup.sql # Cadangan database asli dari laptop untuk dipindah ke Cloud.
```

## Peran Masing-Masing Bagian
1.  **`models/`**: Jika abang ingin menambah kolom di database atau merubah logika hitung-hitungan di belakang layar, di sinilah tempatnya.
2.  **`static/src/xml/`**: Jika abang ingin menambah elemen visual (misal: kotak input baru di layar bayar), abang buat filenya di sini.
3.  **`static/src/js/`**: File di sini yang memberikan "nyawa" pada elemen XML. Misal: Saat input di XML diisi, JS yang akan mengirim datanya ke database.
4.  **`static/src/scss/`**: File ini yang membuat tampilan Odoo abang dari yang tadinya "biasa saja" menjadi "premium" dengan warna Navy dan Orange.
