# 🤖 Artificial Intelligence Powered Bank Assistant

Bu proje, Yapay Zeka dersi kapsamında geliştirilmiştir. Banka müşterilerinin finansal ve demografik verilerini analiz ederek krediye uygunluk seviyelerini ve kredi skorlarını tahmin eden yapay zeka destekli akıllı bir bankacılık ve finansal asistan sistemidir. 

Model geliştirme sürecinde karşılaşılan veri yetersizliği ve sınıf dengesizliği problemleri, SMOTE (Synthetic Minority Over-sampling Technique) yöntemiyle aşılmış; tahminleme aşamasında ise Doğrusal Regresyon ve optimize edilmiş Rastgele Orman (Random Forest Regressor) algoritmaları kullanılmıştır.

---
### 👥 Proje Ekibi
Yasemin Acar
Fatma Gül Doğtaş
Nisanur Kurt
Zeynep Dursun
---
## 📸 Ekran Görüntüleri & Arayüz

[Click](https://yaseminacarr.github.io/Artificial-Intelligence-Powered-Bank-Assistan/)

### Kredi Notu Hesaplama Modülü
Kullanıcıların gelir, varlık, borç, eğitim ve medeni durum bilgilerini girerek makine öğrenmesi algoritmalarıyla kredi notu hesaplamasını ve uygunluk analizini sağlayan arayüz:

<p align="center">
  <img width="567" height="868" alt="Görsel" src="https://github.com/user-attachments/assets/ec26c4f0-a895-4160-97c8-51c3a9390f95" />
</p>

---

## 🚀 Temel Özellikler

- **🧠 Makine Öğrenmesi ile Kredi Skoru Tahmini:** `BankAssistantModeling.py` dosyası içerisinde yer alan Linear Regression ve optimize edilmiş Random Forest Regressor algoritmalarıyla yüksek doğrulukta skorlama.
- **⚖️ SMOTE Desteği:** Sınıf dengesizliğini ortadan kaldırmak için sentetik veri türetme yaklaşımları.
- **📊 Kredi Risk ve Uygunluk Sınıflandırması:** Kredi notuna göre "Çok Riskli", "Orta Riskli", "Az Riskli", "İyi" ve "Çok İyi" olmak üzere kademeli risk analizi .
- **💡 Akıllı Kredi Önerisi ve Hesaplama:** Kullanıcının gelir, varlık ve borç durumuna göre özel faiz oranları ve limitlerle kredi önerisi ve hesaplama modülü .
- **💻 Web Arayüzü:** Kullanıcıların tarayıcı üzerinden kolayca verilerini girip sonuç alabileceği web sayfaları .

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Dil:** Python[cite: 1]
* **Veri Analizi & İşleme:** Pandas, NumPy, SciPy
* **Makine Öğrenmesi:** Scikit-Learn (`LinearRegression`, `RandomForestRegressor`, `StandardScaler`, `SimpleImputer`, `LabelEncoder`)
* **Veri Dengeleme:** SMOTE
* **Veri Toplama & Arayüz:** Google Forms, Excel, HTML

---

## 📂 Proje Dosya Yapısı

```text
Artificial-Intelligence-Powered-Bank-Assistant/
│
├── BankAssistantModeling.py     # Model eğitimi (Linear Regression & Random Forest)
├── bankaverileri.xlsx           # Ham anket veri seti
├── bankaverileri_smote.xlsx     # SMOTE ile dengelenmiş ve artırılmış veri seti
├── CreditScoreClassification.py # Kredi durum sınıflandırma ve öneri modülü
├── CreditScoreCode.py           # Kredi notu hesaplama formülleri ve girdi modülü
├── SMOTE_Code.py                # SMOTE veri dengeleme kodları
├── index.html                   # Web arayüzü ana sayfa
├── website.html                 # Web arayüzü uygulama sayfası
└── README.md                    # Proje dokümantasyonu
```
