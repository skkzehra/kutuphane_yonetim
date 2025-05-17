import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mysql
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime

# Veritabanı bağlantısı
def connect_db():
    try:
        return mysql.connect(
            host="localhost",
            user="root",
            password="15082005",
            database="kutuphane_yönetim"
        )
    except mysql.Error as e:
        messagebox.showerror("Hata", f"Veritabanı bağlantısı başarısız: {e}")
        return None

# Veritabanı tablolarını oluştur
def create_tables():
    db = connect_db()
    if db is None:
        return
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uyeler (
            uye_id INT AUTO_INCREMENT PRIMARY KEY,
            ad VARCHAR(50) NOT NULL,
            soyad VARCHAR(50) NOT NULL,
            sifre VARCHAR(50) NOT NULL,
            kimlik_no CHAR(11) NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitaplar (
            kitap_id INT AUTO_INCREMENT PRIMARY KEY,
            ad VARCHAR(100) NOT NULL,
            yazar VARCHAR(100) NOT NULL,
            durum ENUM('müsait', 'ödünç') DEFAULT 'müsait'
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS odunc (
            odunc_id INT AUTO_INCREMENT PRIMARY KEY,
            kitap_id INT,
            uye_id INT,
            odunc_tarihi DATE,
            iade_tarihi DATE,
            FOREIGN KEY (kitap_id) REFERENCES kitaplar(kitap_id),
            FOREIGN KEY (uye_id) REFERENCES uyeler(uye_id)
        )
    """)
    db.commit()
    cursor.close()
    db.close()

# Arka plan görseli ekleme fonksiyonu
def set_background(window, image_path, width, height):
    try:
        image = Image.open(image_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        background_label = tk.Label(window, image=photo)
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lower()
    except Exception as e:
        print(f"Arka plan görseli yüklenemedi: {e}")

# Pencereyi ortalama fonksiyonu
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# İkon dosyalarını yükleme fonksiyonu
icon_images = {
    "add": "icon/add_icon.png",
    "search": "icon/search_icon.png",
    "borrow": "icon/borrow_icon.png",
    "return": "icon/return_icon.png",
    "profile": "icon/profile_icon.png",
    "login": "icon/login_icon.png",
    "register": "icon/register_icon.png",
    "list": "icon/list_icon.png"  
}

def load_icon(icon_key, size=(20, 20)):
    try:
        image_path = icon_images.get(icon_key, "default_icon.png")
        image = Image.open(image_path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=image, dark_image=image, size=size)
    except FileNotFoundError:
        print(f"İkon dosyası bulunamadı ({icon_key}): {image_path}")
        return None
    except Exception as e:
        print(f"İkon yüklenemedi ({icon_key}): {e}")
        return None

class LoginScreen:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Kütüphane Yönetim Sistemi - Giriş")
        center_window(self.root, 400, 350)
        self.root.resizable(False, False)
        create_tables()

        set_background(self.root, "image/log_bg.png", 400, 350)

        ctk.CTkLabel(self.root, text="Ad:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.entry_ad = ctk.CTkEntry(self.root, width=200)
        self.entry_ad.pack(pady=5)

        ctk.CTkLabel(self.root, text="Şifre:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.entry_sifre = ctk.CTkEntry(self.root, show="*", width=200)
        self.entry_sifre.pack(pady=5)

        ctk.CTkButton(
            self.root,
            text="Giriş Yap",
            command=self.login,
            image=load_icon("login"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).pack(pady=10)

        ctk.CTkButton(
            self.root,
            text="Kayıt Ol",
            command=self.open_register,
            image=load_icon("register"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).pack(pady=10)

        self.root.mainloop()

    def login(self):
        ad = self.entry_ad.get()
        sifre = self.entry_sifre.get()

        if not ad or not sifre:
            messagebox.showerror("Hata", "Ad ve şifre boş olamaz!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        cursor.execute("SELECT uye_id FROM uyeler WHERE ad = %s AND sifre = %s", (ad, sifre))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            self.root.destroy()
            KutuphaneUygulamasi(user_id=user[0])
        else:
            messagebox.showerror("Hata", "Ad veya şifre yanlış!")

    def open_register(self):
        self.register_window = ctk.CTkToplevel(self.root)
        self.register_window.title("Üye Kayıt")
        center_window(self.register_window, 300, 350)
        self.register_window.resizable(False, False)
        set_background(self.register_window, "bg.png", 300, 350)

        ctk.CTkLabel(self.register_window, text="Ad:", font=("Arial", 12), fg_color="transparent").pack(pady=5)
        self.reg_ad = ctk.CTkEntry(self.register_window, width=200)
        self.reg_ad.pack(pady=5)

        ctk.CTkLabel(self.register_window, text="Soyad:", font=("Arial", 12), fg_color="transparent").pack(pady=5)
        self.reg_soyad = ctk.CTkEntry(self.register_window, width=200)
        self.reg_soyad.pack(pady=5)

        ctk.CTkLabel(self.register_window, text="Şifre:", font=("Arial", 12), fg_color="transparent").pack(pady=5)
        self.reg_sifre = ctk.CTkEntry(self.register_window, show="*", width=200)
        self.reg_sifre.pack(pady=5)

        ctk.CTkLabel(self.register_window, text="Kimlik No (11 hane):", font=("Arial", 12), fg_color="transparent").pack(pady=5)
        self.reg_kimlik = ctk.CTkEntry(self.register_window, width=200)
        self.reg_kimlik.pack(pady=5)

        ctk.CTkButton(
            self.register_window,
            text="Kayıt Ol",
            command=self.register,
            image=load_icon("register"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).pack(pady=10)

    def register(self):
        ad = self.reg_ad.get()
        soyad = self.reg_soyad.get()
        sifre = self.reg_sifre.get()
        kimlik_no = self.reg_kimlik.get()

        if not ad or not soyad or not sifre or not kimlik_no:
            messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır!")
            return

        if len(kimlik_no) != 11 or not kimlik_no.isdigit():
            messagebox.showerror("Hata", "Kimlik numarası 11 haneli ve sadece rakamlardan oluşmalıdır!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO uyeler (ad, soyad, sifre, kimlik_no) VALUES (%s, %s, %s, %s)", (ad, soyad, sifre, kimlik_no))
            db.commit()
            messagebox.showinfo("Başarılı", "Kayıt tamamlandı!")
            self.register_window.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Kayıt başarısız: {e}")
        finally:
            cursor.close()
            db.close()

class KutuphaneUygulamasi:
    def __init__(self, user_id):
        self.user_id = user_id
        self.pencere = ctk.CTk()
        self.current_window = None  # Açık olan alt pencereyi takip etmek için
        self.setup_ui()
        self.pencere.mainloop()

    def close_current_window(self):
        if self.current_window:
            self.current_window.destroy()
            self.current_window = None

    def setup_ui(self):
        self.pencere.title("Kütüphane Yönetim Sistemi")
        center_window(self.pencere, 950, 600)
        self.pencere.resizable(False, False)
        set_background(self.pencere, "image/bg.png", 950, 600)

        # Menü kutuları alt alta
        self.menu_frame = ctk.CTkFrame(self.pencere, fg_color="transparent")
        self.menu_frame.pack(pady=20)

        btn_info = [
            ("Kitap Ekle", self.kitap_ekle_ekrani, "add"),
            ("Kitap Ara", self.kitap_ara_ekrani, "search"),
            ("Ödünç Al", self.odunc_al_ekrani, "borrow"),
            ("İade Et", self.iade_et_ekrani, "return"),
            ("Üye Profili", self.uye_profili_ekrani, "profile"),
            ("Kitap Listesi", self.kitap_listesi_ekrani, "list")  # Yeni menü
        ]
        for text, command, icon in btn_info:
            ctk.CTkButton(
                self.menu_frame,
                text=text,
                command=command,
                image=load_icon(icon),
                compound="left",
                width=300,
                height=60,
                corner_radius=10,
                font=("Arial", 14, "bold"),
                fg_color="#FF0000",
                bg_color="transparent",
                hover_color="#520303",
                text_color="white",
                border_width=0  # Kenarlık kalınlığını sıfırlayarak gri çerçeve önleme
            ).pack(pady=10, padx=20)

    def kitap_listesi_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("Kitap Listesi")
        center_window(self.current_window, 600, 400)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        # Tabloyu oluştur
        columns = ("Kitap Adı", "Yazar", "Durum")
        tree = ttk.Treeview(self.current_window, columns=columns, show="headings")
        tree.heading("Kitap Adı", text="Kitap Adı")
        tree.heading("Yazar", text="Yazar")
        tree.heading("Durum", text="Durum")
        tree.column("Kitap Adı", width=200)
        tree.column("Yazar", width=200)
        tree.column("Durum", width=100)
        tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Veritabanından kitapları çek
        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT ad, yazar, durum FROM kitaplar")
            kitaplar = cursor.fetchall()
            for kitap in kitaplar:
                durum = "Kiralanmış" if kitap[2] == "ödünç" else "Müsait"
                tree.insert("", "end", values=(kitap[0], kitap[1], durum))
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Kitap listesi alınamadı: {e}")
        finally:
            cursor.close()
            db.close()

    def kitap_ekle_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("Kitap Ekle")
        center_window(self.current_window, 400, 300)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        ctk.CTkLabel(self.current_window, text="Kitap Adı:", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.entry_kitap_ad = ctk.CTkEntry(self.current_window, width=200)
        self.entry_kitap_ad.grid(row=0, column=1, pady=5)

        ctk.CTkLabel(self.current_window, text="Yazar:", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=5, padx=10, sticky="e")
        self.entry_yazar = ctk.CTkEntry(self.current_window, width=200)
        self.entry_yazar.grid(row=1, column=1, pady=5)

        ctk.CTkButton(
            self.current_window,
            text="Kitap Ekle",
            command=self.kitap_ekle,
            image=load_icon("add"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def kitap_ekle(self):
        ad = self.entry_kitap_ad.get()
        yazar = self.entry_yazar.get()
        if not ad or not yazar:
            messagebox.showerror("Hata", "Kitap adı ve yazar zorunludur!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO kitaplar (ad, yazar) VALUES (%s, %s)", (ad, yazar))
            db.commit()
            messagebox.showinfo("Başarılı", "Kitap eklendi!")
            self.current_window.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Kitap eklenemedi: {e}")
        finally:
            cursor.close()
            db.close()

    def kitap_ara_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("Kitap Ara")
        center_window(self.current_window, 400, 200)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        ctk.CTkLabel(self.current_window, text="Kitap Adı:", font=("Arial", 12, "bold")).pack(pady=10)
        self.arama_entry = ctk.CTkEntry(self.current_window, width=200)
        self.arama_entry.pack(pady=5)

        ctk.CTkButton(
            self.current_window,
            text="Ara",
            command=self.kitap_ara,
            image=load_icon("search"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).pack(pady=10)

        self.sonuc_label = ctk.CTkLabel(self.current_window, text="", font=("Arial", 12))
        self.sonuc_label.pack(pady=5)

    def kitap_ara(self):
        arama_terimi = self.arama_entry.get().lower()
        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT ad, yazar, durum FROM kitaplar WHERE LOWER(ad) LIKE %s", (f"%{arama_terimi}%",))
            sonuclar = cursor.fetchall()
            if sonuclar:
                sonuc_metni = "Bulunan Kitaplar:\n" + "\n".join([f"{ad} - {yazar} ({'Kiralanmış' if durum == 'ödünç' else 'Müsait'})" for ad, yazar, durum in sonuclar])
            else:
                sonuc_metni = "Kitap bulunamadı."
            self.sonuc_label.configure(text=sonuc_metni)
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Arama hatası: {e}")
        finally:
            cursor.close()
            db.close()

    def odunc_al_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("Ödünç Al")
        center_window(self.current_window, 400, 300)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        ctk.CTkLabel(self.current_window, text="Kitap Adı:", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.odunc_kitap = ctk.CTkEntry(self.current_window, width=200)
        self.odunc_kitap.grid(row=0, column=1, pady=5)

        ctk.CTkButton(
            self.current_window,
            text="Ödünç Al",
            command=self.odunc_al,
            image=load_icon("borrow"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).grid(row=1, column=0, columnspan=2, pady=10)

    def odunc_al(self):
        kitap_ad = self.odunc_kitap.get()
        if not kitap_ad:
            messagebox.showerror("Hata", "Kitap adı girilmedi!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT kitap_id, durum FROM kitaplar WHERE ad = %s", (kitap_ad,))
            kitap = cursor.fetchone()
            if not kitap or kitap[1] != 'müsait':
                messagebox.showerror("Hata", "Kitap mevcut değil veya ödünç alınmış!")
                return
            cursor.execute("INSERT INTO odunc (kitap_id, uye_id, odunc_tarihi) VALUES (%s, %s, CURDATE())", (kitap[0], self.user_id))
            cursor.execute("UPDATE kitaplar SET durum = 'ödünç' WHERE kitap_id = %s", (kitap[0],))
            db.commit()
            messagebox.showinfo("Başarılı", "Kitap ödünç alındı!")
            self.current_window.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Ödünç alma hatası: {e}")
        finally:
            cursor.close()
            db.close()

    def iade_et_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("İade Et")
        center_window(self.current_window, 400, 200)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        ctk.CTkLabel(self.current_window, text="Kitap Adı:", font=("Arial", 12, "bold")).pack(pady=10)
        self.iade_kitap = ctk.CTkEntry(self.current_window, width=200)
        self.iade_kitap.pack(pady=5)

        ctk.CTkButton(
            self.current_window,
            text="İade Et",
            command=self.iade_et,
            image=load_icon("return"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#FF0000",
            hover_color="#CC0000",
            bg_color="transparent"
        ).pack(pady=10)

    def iade_et(self):
        kitap_ad = self.iade_kitap.get()
        if not kitap_ad:
            messagebox.showerror("Hata", "Kitap adı girilmedi!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT k.kitap_id FROM kitaplar k JOIN odunc o ON k.kitap_id = o.kitap_id WHERE k.ad = %s AND o.uye_id = %s AND o.iade_tarihi IS NULL", (kitap_ad, self.user_id))
            odunc = cursor.fetchone()
            if not odunc:
                messagebox.showerror("Hata", "Bu kitap size ödünç verilmemiş!")
                return
            cursor.execute("UPDATE kitaplar SET durum = 'müsait' WHERE kitap_id = %s", (odunc[0],))
            cursor.execute("UPDATE odunc SET iade_tarihi = CURDATE() WHERE kitap_id = %s AND uye_id = %s AND iade_tarihi IS NULL", (odunc[0], self.user_id))
            db.commit()
            messagebox.showinfo("Başarılı", "Kitap iade edildi!")
            self.current_window.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"İade hatası: {e}")
        finally:
            cursor.close()
            db.close()

    def uye_profili_ekrani(self):
        self.close_current_window()
        self.current_window = ctk.CTkToplevel(self.pencere)
        self.current_window.title("Üye Profili")
        center_window(self.current_window, 400, 300)
        self.current_window.resizable(False, False)
        self.current_window.attributes('-topmost', True)

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT ad, soyad, kimlik_no FROM uyeler WHERE uye_id = %s", (self.user_id,))
        uye = cursor.fetchone()
        cursor.execute("SELECT k.ad FROM kitaplar k JOIN odunc o ON k.kitap_id = o.kitap_id WHERE o.uye_id = %s AND o.iade_tarihi IS NULL", (self.user_id,))
        odunc_kitaplar = cursor.fetchall()
        cursor.close()
        db.close()

        ctk.CTkLabel(self.current_window, text=f"Ad: {uye[0]}", font=("Arial", 12, "bold")).pack(pady=5)
        ctk.CTkLabel(self.current_window, text=f"Soyad: {uye[1]}", font=("Arial", 12, "bold")).pack(pady=5)
        ctk.CTkLabel(self.current_window, text=f"Kimlik No: {uye[2]}", font=("Arial", 12, "bold")).pack(pady=5)
        ctk.CTkLabel(self.current_window, text="Ödünç Alınan Kitaplar:", font=("Arial", 12, "bold")).pack(pady=5)
        if odunc_kitaplar:
            kitap_listesi = "\n".join([k[0] for k in odunc_kitaplar])
        else:
            kitap_listesi = "Ödünç alınmış kitap yok."
        ctk.CTkLabel(self.current_window, text=kitap_listesi, font=("Arial", 12)).pack(pady=5)

if __name__ == "__main__":
    LoginScreen()