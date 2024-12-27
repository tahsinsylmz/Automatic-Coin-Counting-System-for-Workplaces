# İş Yerleri için Otomatik Bozuk Para Sayma Sistemi

Bu proje, marketler, bankalar ve diğer iş yerlerinde bozuk para sayma işlemlerini otomatikleştirerek zaman tasarrufu sağlamayı ve doğruluğu artırmayı amaçlayan bir sistem sunmaktadır. Sistem, **OpenCV** ve **ColorFinder** gibi güçlü görüntü işleme araçlarını kullanarak, bozuk paraların boyut ve renk özelliklerini analiz eder ve toplam değerlerini doğru bir şekilde hesaplar.

---

## 🚀 Özellikler

- **Görüntü İşleme Teknikleri:**
  - Gaussian Blur, Canny kenar algılama ve morfolojik işlemlerle yüksek doğrulukta görüntü analizi.
- **Gerçek Zamanlı Çalışma:**
  - Ortalama 30 FPS hızında, canlı kamera girdileriyle bozuk para tespiti.
- **Esnek Parametreler:**
  - Kullanıcıların sistem parametrelerini ayarlayabileceği kullanıcı dostu bir arayüz.
- **Uyarlanabilirlik:**
  - Farklı aydınlatma koşullarında ve para birimlerinde kullanılabilir.
- **Modüler Yapı:**
  - Kolay entegrasyon ve özelleştirilebilir algoritmalar.

---

## 📂 Kullanım Alanları

- Marketler, bankalar ve finans kuruluşlarında otomasyon.
- Otomatik bozuk para ayrıştırma ve geri dönüşüm projeleri.
- Eğitim amaçlı görüntü işleme ve sınıflandırma sistemlerinin geliştirilmesi.

---

## 📦 Kurulum

### Gereksinimler:
- Python 3.8 veya üstü
- OpenCV
- ColorFinder (CvZone Modülü)
- NumPy

### Adımlar:
1. **Proje Dosyalarını İndirin:**
   ```bash
   git clone https://github.com/username/coin-counting-system.git
   cd coin-counting-system
