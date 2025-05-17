# 📚 Kütüphane Yönetim Sistemi - Python OOP GUI Uygulaması

<p align="center">
  <img src="giriş_ekranı.png" alt="Giriş Ekranı" width="400">
  <img src="ana_menu.png" alt="Ana Menü" width="400">
</p>

Bu uygulama, Python programlama dili ve grafik kullanıcı arayüzü (GUI) teknolojileri kullanılarak geliştirilmiş kapsamlı bir kütüphane otomasyon sistemidir. Nesne yönelimli programlama (OOP) prensiplerine dayanarak geliştirilmiş olup, MySQL veritabanı ile entegre çalışmaktadır.

## 🧱 Kullanılan Teknolojiler

* **Python 3.x:** Uygulamanın temelini oluşturan, okunabilir ve güçlü bir programlama dili.
* **MySQL:** Güvenilir ve yaygın olarak kullanılan açık kaynaklı veritabanı yönetim sistemi.
* **Tkinter & CustomTkinter:** Modern ve özelleştirilebilir kullanıcı arayüzleri oluşturmak için kullanılan GUI kütüphaneleri. CustomTkinter, Tkinter'in görünümünü iyileştirerek daha çekici bir deneyim sunar.
* **Pillow (PIL):** Görüntü işleme yetenekleri sağlayan, ikonlar ve arka plan görselleri gibi görsel öğelerin yönetimi için kullanılır.

## 🧠 Nesne Yönelimli Programlama (OOP) Yapısı

Uygulama, OOP'nin temel prensiplerini benimseyerek modüler, esnek ve bakımı kolay bir mimari sunar:

* **🔒 Encapsulation (Kapsülleme):** Her modül, kendi verisi ve bu veriye erişim sağlayan metotlarla birlikte kapsüllenmiştir. Bu, veri güvenliğini artırır ve istenmeyen değişiklikleri önler.
* **📜 Inheritance (Kalıtım):** Sistem, ortak özellikleri ve davranışları paylaşan sınıflar arasında kalıtım ilişkileri kurarak kod tekrarını en aza indirir. Örneğin, farklı pencere türleri (kitap ekleme, kitap arama vb.) ortak bir temel sınıftan türetilerek, temel GUI özelliklerini devralır.
* **✨ Polymorphism (Çok Biçimlilik):** Farklı nesnelerin aynı metot çağrısına farklı şekillerde yanıt verebilmesi prensibidir. Uygulamada, örneğin, farklı veri giriş ekranları (kitap ekleme, üye kaydı) benzer "kaydet" veya "görüntüle" gibi işlemleri farklı biçimlerde uygulayarak çok biçimliliğe örnek teşkil eder.
* **🧩 Abstraction (Soyutlama):** Karmaşık sistem detaylarının kullanıcıdan gizlenerek, sadece gerekli işlevselliğin sunulmasıdır. Veritabanı işlemleri, GUI bileşenlerinin detaylı yapılandırması ve kullanıcı etkileşimlerinin yönetimi gibi arka plandaki süreçler, soyut sınıflar ve metotlar aracılığıyla basitleştirilmiştir.

## ⚙️ Özellikler

* **👤 Kullanıcı Girişi & Kayıt Olma:**
  <p align="center">
    <img src="giriş_ekranı.png" alt="Kullanıcı Girişi Ekranı" width="400">
  </p>
  Güvenli kullanıcı yönetimi ile sisteme erişimi kontrol altına alır. Kullanıcılar, kendi hesaplarını oluşturabilir ve geçerli kimlik bilgileriyle sisteme giriş yapabilir.

* **📄 Üye Kayıt ve Yönetimi:** Üye bilgilerinin (ad, soyad, kimlik no vb.) kaydedilmesi, güncellenmesi ve yönetilmesi.

* **📚 Kitap Ekleme, Arama ve Listeleme:**
  <p align="center">
    <img src="kitap_arama.png" alt="Kitap Arama Ekranı" width="400">
    <img src="kitap_listesi.png" alt="Kitap Listesi Ekranı" width="600">
  </p>
  Kitap bilgilerinin (ad, yazar, durum vb.) sisteme eklenmesi, mevcut kitapların listelenmesi ve aranması.

* **📆 Kitap Ödünç Alma ve İade Etme:**
  <p align="center">
    <img src="kitap_odunc_alma.png" alt="Kitap Ödünç Alma Ekranı" width="400">
  </p>
  Üyelere kitap ödünç verme ve iade alma işlemlerinin gerçekleştirilmesi, ödünç sürelerinin takibi.

* **📜 Ödünç Geçmişi ve Aktif Ödünçler:** Geçmiş ödünç kayıtlarının görüntülenmesi ve şu anda devam eden aktif ödünç işlemlerinin takibi.

* **💾 MySQL Veritabanı Entegrasyonu:** Verilerin güvenli ve kalıcı olarak saklanmasını sağlayan MySQL veritabanı ile sorunsuz entegrasyon.

* **🌙 Dark Mode Desteği:** Kullanıcı tercihine göre ayarlanabilen, göz yorgunluğunu azaltan modern karanlık tema desteği.

* **👤 Üye Profili:**
  <p align="center">
    <img src="uye_profili.png" alt="Üye Profili Ekranı" width="400">
  </p>
  Kullanıcıların kendi profil bilgilerini görüntüleyebildiği ve ödünç aldıkları kitapları takip edebildiği bölüm.

## 🗃️ Veritabanı Yapısı

Uygulama, verileri düzenli ve verimli bir şekilde saklamak için aşağıdaki tabloları kullanır. Tablolar, uygulama ilk kez çalıştırıldığında otomatik olarak oluşturulur:

| Tablo          | Açıklama                     |
| -------------- | ---------------------------- |
| `uyeler`       | Üye bilgileri                |
| `kitaplar`     | Kitap bilgileri              |
| `odunc`        | Ödünç alma/iade bilgileri   |

## 🚀 Kurulum ve Çalıştırma

1.  Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install customtkinter pillow mysql-connector-python
    ```

2.  Veritabanı bağlantı ayarlarını (host, user, password) `connect_db()` fonksiyonunda güncelleyin.
3.  Uygulamayı çalıştırın:

    ```bash
    python kütüphane_yönetim.py  # veya uygulamanızın adı
    ```

## 👨‍💻 Geliştirici

\[Zehra Işık]

\[isikkzehraa@gmail.com]

Sürüm: 1.0
