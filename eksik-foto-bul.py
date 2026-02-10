import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# --- AYARLAR ---
SITE_DIR = "motorhikayesi_final_tertemiz"  # HTML dosyalarının olduğu klasör
UPLOADS_DIR = "wp-content/uploads"        # Görsellerin fiziksel olarak durduğu klasör
REPORT_DIR = "foto-eksik"
REPORT_FILE = "eksik-foto.txt"

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

def check_missing_images():
    missing_images = set()
    html_files = [f for f in os.listdir(SITE_DIR) if f.endswith(".html")]

    print(f"{len(html_files)} sayfa taranıyor...")

    for file in html_files:
        file_path = os.path.join(SITE_DIR, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            images = soup.find_all('img')

            for img in images:
                src = img.get('src')
                if not src:
                    continue

                # Sadece site içi (uploads klasöründeki) resimleri kontrol et
                if "wp-content/uploads" in src:
                    # URL'den temiz dosya yolunu al (parametreleri temizle)
                    parsed_path = urlparse(src).path
                    # wp-content/uploads kısmından sonrasını al
                    relative_img_path = parsed_path.split("wp-content/uploads/")[-1]
                    
                    # Fiziksel konumu kontrol et
                    full_physical_path = os.path.join(UPLOADS_DIR, relative_img_path)
                    
                    if not os.path.exists(full_physical_path):
                        missing_images.add(src)

    # Raporu kaydet
    report_path = os.path.join(REPORT_DIR, REPORT_FILE)
    with open(report_path, 'w', encoding='utf-8') as f:
        if missing_images:
            f.write("\n".join(sorted(missing_images)))
            print(f"Bitti! {len(missing_images)} eksik görsel bulundu.")
            print(f"Rapor şurada: {report_path}")
        else:
            f.write("Hiç eksik görsel bulunamadı.")
            print("Tebrikler! Tüm görseller yerinde.")

if __name__ == "__main__":
    check_missing_images()