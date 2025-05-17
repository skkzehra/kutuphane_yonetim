# 📚 Kütüphane Yönetim Sistemi - Python OOP GUI Uygulaması

<p align="center">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.48.53.png" alt="Giriş Ekranı" width="400">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.49.41.png" alt="Ana Menü" width="400">
</p>

Bu uygulama, Python programlama dili ve grafik kullanıcı arayüzü (GUI) teknolojileri kullanılarak geliştirilmiş kapsamlı bir kütüphane otomasyon sistemidir. Nesne yönelimli programlama (OOP) prensiplerine dayanarak geliştirilmiş olup, MySQL veritabanı ile entegre çalışmaktadır.

---

## 🧱 Kullanılan Teknolojiler

- **Python 3.x**
- **MySQL**
- **Tkinter & CustomTkinter**
- **Pillow (PIL)**

---

## 🧠 Nesne Yönelimli Programlama (OOP) Yapısı

- 🔒 **Encapsulation (Kapsülleme)**
- 📜 **Inheritance (Kalıtım)**
- ✨ **Polymorphism (Çok Biçimlilik)**
- 🧩 **Abstraction (Soyutlama)**

---

## ⚙️ Özellikler

### 👤 Kullanıcı Girişi & Kayıt Olma
<p align="center">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.48.53.png" alt="Kullanıcı Girişi Ekranı" width="400">
</p>

- Güvenli kullanıcı yönetimi
- Kayıt & Giriş işlemleri

---

### 📄 Üye Kayıt ve Yönetimi

- Üye bilgilerini ekleme, güncelleme ve listeleme

---

### 📚 Kitap Ekleme, Arama ve Listeleme

<p align="center">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.50.39.png" alt="Kitap Arama Ekranı" width="400">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.52.57.png" alt="Kitap Listesi Ekranı" width="600">
</p>

- Kitap bilgilerini ekleme
- Arama ve filtreleme özellikleri

---

### 📆 Kitap Ödünç Alma ve İade Etme

<p align="center">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.51.24.png" alt="Kitap Ödünç Alma Ekranı" width="400">
</p>

- Üyelere kitap ödünç verme / iade alma
- Ödünç süresi takibi

---

### 📜 Ödünç Geçmişi ve Aktif Ödünçler

- Geçmiş işlemlerin ve aktif ödünçlerin yönetimi

---

### 💾 MySQL Veritabanı Entegrasyonu

- Güvenli ve hızlı veri saklama altyapısı

---

### 🌙 Dark Mode Desteği

- Kullanıcı tercihlerine göre tema seçimi

---

### 👤 Üye Profili

<p align="center">
  <img src="https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.52.25.png" alt="Üye Profili Ekranı" width="400">
</p>

- Profil görüntüleme
- Ödünç alınan kitaplar listesi

---

## 🗃️ Veritabanı Yapısı

| Tablo      | Açıklama                        |
|------------|---------------------------------|
| `uyeler`   | Üye bilgileri                   |
| `kitaplar` | Kitap bilgileri                 |
| `odunc`    | Ödünç alma / iade kayıtları     |

---

## 🚀 Kurulum ve Çalıştırma

### 1. Gerekli kütüphaneleri yükleyin

```bash
pip install customtkinter pillow mysql-connector-python
