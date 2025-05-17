# 📚 Kütüphane Yönetim Sistemi - Python OOP GUI Uygulaması

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

- 👤 Kullanıcı Girişi ve Kayıt Olma
- 📄 Üye Ekleme, Güncelleme, Silme
- 📚 Kitap Ekleme, Arama, Listeleme
- 📆 Kitap Ödünç Alma ve İade Etme
- 📜 Aktif ve Geçmiş Ödünç Kayıtları
- 🌙 Dark Mode Desteği
- 💾 MySQL Veritabanı Entegrasyonu
- 👤 Üye Profil Görüntüleme

---

## 📷 Uygulama Arayüzünden Görseller

### 🔐 Giriş Ekranı
![Giriş Ekranı](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.48.53.png)

---

### 🏠 Ana Menü
![Ana Menü](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.49.41.png)

---

### 👤 Üye Profili
![Üye Profili](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.52.25.png)

---

### 📚 Kitap Ekleme
![Kitap Ekleme](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.50.12.png)

---

### 📆 Kitap Ödünç Alma
![Kitap Ödünç Alma](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.51.24.png)

---

### 🗂️ İade Et
![İade Et](https://github.com/skkzehra/kutuphane_yonetim/blob/main/kütüphane_yönetimi/ss/Ekran%20Resmi%202025-05-17%2013.51.54.png)

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
