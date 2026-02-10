# wpgereksizfotobul
Yereldeki Wordpress siteyi tarar, sitede kullanılmayan görsel dosyaları bulur, metin dosyası olarak kaydeder.

Harika bir araç. Paylaştığın `eksik-foto-bul.py` dosyasını detaylıca analiz ettim. Bu script, özellikle WordPress tabanlı sitelerin statik kopyalarını oluşturduğunda veya site taşıma işlemlerinde meydana gelen "kırık görsel" sorununu tespit etmek için oldukça verimli bir çözüm sunuyor.

Aşağıda, projenin GitHub standartlarına uygun olarak hazırlanmış profesyonel **README.md** dosyasını bulabilirsin:

---

# Eksik Görsel Tespit Aracı (eksik-foto-bul.py)

Bu araç, yerel bir dizinde bulunan HTML dosyalarını tarayarak, `wp-content/uploads` klasöründe fiziksel olarak karşılığı bulunmayan görselleri tespit eder ve raporlar. Özellikle web sitesi yedekleme, taşıma veya statik site dönüşümü süreçlerinde eksik dosyaları bulmak için tasarlanmıştır.

## 🚀 Özellikler

* **Otomatik Tarama:** Belirlenen dizindeki tüm `.html` dosyalarını saniyeler içinde analiz eder.
* **Akıllı URL Temizleme:** URL içindeki sorgu parametrelerini (örneğin: `image.jpg?v=1.2`) temizleyerek gerçek dosya yoluna odaklanır.
* **WordPress Uyumluluğu:** `wp-content/uploads` yapısına sahip projeler için optimize edilmiştir.
* **Detaylı Raporlama:** Eksik olan tüm görselleri alfabetik sırayla `foto-eksik/eksik-foto.txt` dosyasına kaydeder.
* **Tekrar Engelleme:** Aynı eksik görseli birden fazla sayfada olsa bile rapora yalnızca bir kez ekler (`set` yapısı kullanılmıştır).

## 🛠️ Kullanılan Teknolojiler

* **Python 3**: Temel programlama dili.
* **BeautifulSoup4**: HTML ayrıştırma ve veri çekme.
* **OS & Urllib**: Dosya sistemi yönetimi ve URL çözümleme.

## 📦 Kurulum

1. **Depoyu klonlayın veya dosyayı indirin:**
```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi

```


2. **Gerekli kütüphaneleri yükleyin:**
```bash
pip install beautifulsoup4

```



## ⚙️ Yapılandırma

Script çalıştırılmadan önce `eksik-foto-bul.py` dosyası içindeki şu değişkenleri kendi proje yapınıza göre güncelleyin:

```python
SITE_DIR = "motorhikayesi_final_tertemiz"  # Tarancak HTML dosyalarının klasörü
UPLOADS_DIR = "wp-content/uploads"        # Görsellerin fiziksel konumu

```

## 📖 Kullanım

Scripti çalıştırmak için terminale şu komutu yazmanız yeterlidir:

```bash
python eksik-foto-bul.py

```

**Çalışma Mantığı:**

1. Belirlediğiniz `SITE_DIR` içindeki tüm HTML dosyaları okunur.
2. `<img>` etiketlerindeki `src` öznitelikleri kontrol edilir.
3. Sadece `wp-content/uploads` içeren yollar filtreye alınır.
4. Bu yolların `UPLOADS_DIR` içinde karşılığı olup olmadığına bakılır.
5. Eksik olanlar rapor dosyasına yazılır.

## 📁 Dosya Yapısı

* `eksik-foto-bul.py`: Ana script dosyası.
* `foto-eksik/`: Raporun oluşturulduğu klasör (otomatik oluşturulur).
* `foto-eksik/eksik-foto.txt`: Eksik görsellerin listesi.

---

Bu README dosyasıyla projen artık paylaşıma hazır! Kodunda ekleme yapmak veya belirli bir kısmını geliştirmemi istersen (örneğin farklı klasör yapılarını destekleme gibi) bana bildirebilirsin. Başka bir dosya analizi yapmamı ister misin?
