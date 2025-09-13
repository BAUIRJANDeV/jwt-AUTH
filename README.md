# 📱 Telefon‑API

Telefon‑API Django & DRF asosida qurilgan backend API bo‘lib, quyidagi funksiyalarni taklif qiladi:

- Foydalanuvchi ro‘yxatdan o‘tishi va login qilishi  
- Mahsulotlar (Phone) ro‘yxatini olish  
- Savatcha (Cart): telefon qo‘shish, miqdorini o‘zgartirish, olib tashlash, savatchani ko‘rish  
- Buyurtma (Order): savatchadagi mahsulotlar asosida buyurtma yaratish, bekor qilish, detallarini ko‘rish  

---

## ⚙️ Texnologiyalar

- Python  
- Django  
- Django REST Framework  
- JWT Authentication  
- SQLite (development uchun)  
- Media fayllar uchun papka: `media/`

---

## 🚀 Loyihani ishga tushirish

```bash
# Repo’ni klonlash
git clone https://github.com/BAUIRJANDeV/Telefon‑API.git
cd Telefon‑API

# Virtual muhit yaratish
python -m venv venv
# Aktivlashtirish (Windows)
venv\Scripts\activate
# Yoki Linux/macOS
source venv/bin/activate

# Kerakli paketlarni o‘rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Media fayllar va statik fayllar sozlamalariga e’tibor bering (settings.py da MEDIA_ROOT, MEDIA_URL)
# Ishga tushurish
python manage.py runserver
🛒 Savatcha (Cart) API
Endpoint	Method	Tavsif
/card/api/cart/	GET	Savatchadagi mahsulotlarni ko‘rish
/card/api/cart/add/	POST	Savatchaga telefon qo‘shish
/card/api/cart/update/	PUT	Miqdorni o‘zgartirish
/card/api/cart/remove/<id>/	DELETE	Mahsulotni savatchadan o‘chirish

📦 Buyurtma (Order) API
Endpoint	Method	Tavsif
/order/api/orders/	GET	Mening buyurtmalarim
/order/api/orders/create/	POST	Buyurtma yaratish
/order/api/orders/<id>/	GET	Buyurtma detali
/order/api/orders/<id>/cancel/	PUT	Buyurtmani bekor qilish