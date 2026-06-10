import os
import pandas as pd
import requests

def download_barcodes():
    csv_file = 'produk_odoo.csv'
    
    if not os.path.exists(csv_file):
        print(f"Error: File {csv_file} tidak ditemukan!")
        return
        
    # Membaca data produk
    df = pd.read_csv(csv_file)
    
    print(f"Memulai proses unduh barcode untuk {len(df)} produk...")
    
    for index, row in df.iterrows():
        name = row['name']
        barcode = str(row['barcode']).strip()
        category = row['categ_id/id']
        
        # Bersihkan nama kategori untuk digunakan sebagai nama folder
        # Menggunakan nama id kategori atau bisa disesuaikan
        folder_name = category.replace('cat_', '').replace('_', ' ').title()
        
        # Buat folder jika belum ada
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Membuat folder baru: {folder_name}")
            
        # Bersihkan nama file dari karakter ilegal
        safe_name = "".join([c for c in name if c.isalpha() or c.isdigit() or c in ' ']).rstrip()
        file_name = f"{safe_name}-{barcode}.png"
        file_path = os.path.join(folder_name, file_name)
        
        # URL API Tec-It Barcode
        url = f"https://barcode.tec-it.com/barcode.ashx?data={barcode}&code=EAN13"
        
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Berhasil mengunduh: {file_path}")
            else:
                print(f"Gagal mengunduh barcode untuk {name} (Status Code: {response.status_code})")
        except Exception as e:
            print(f"Terjadi error saat mengunduh barcode untuk {name}: {e}")

if __name__ == '__main__':
    download_barcodes()
