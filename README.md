# 🎵 SoundCloud Music Streamer

یک وب‌اپلیکیشن ساده و قدرتمند برای جستجو، پخش آنلاین و دانلود موسیقی از SoundCloud با استفاده از Flask و yt-dlp.

## ✨ ویژگی‌ها

- 🔍 **جستجوی قدرتمند**: جستجو در میلیون‌ها آهنگ SoundCloud
- 🎧 **پخش آنلاین**: استریم مستقیم بدون نیاز به دانلود
- 📥 **دانلود MP3**: دانلود آهنگ‌ها با کیفیت بالا
- 🚀 **سرعت بالا**: نتایج سریع و واکنش‌گرای فوری
- 📱 **طراحی ریسپانسیو**: سازگار با موبایل و دسکتاپ
- 🎪 **20 نتیجه**: نمایش تا 20 نتیجه در هر جستجو

## 🛠️ نیازمندی‌ها

### نرم‌افزارها
- Python 3.7+
- FFmpeg (برای تبدیل فرمت فایل‌ها)

### پکیج‌های Python
```bash
pip install flask yt-dlp requests
```

## 📦 نصب

### 1. کلون کردن پروژه
```bash
git clone https://github.com/Qarebaq/Music_Player.git
cd Music_Player
```

### 2. ایجاد محیط مجازی (اختیاری اما توصیه شده)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate     # Windows
```

### 3. نصب پکیج‌ها
```bash
pip install -r requirements.txt
```

### 4. نصب FFmpeg

#### Windows:
1. از [FFmpeg.org](https://ffmpeg.org/download.html) دانلود کنید
2. فایل را extract کرده و path آن را به متغیر محیطی اضافه کنید

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS:
```bash
brew install ffmpeg
```

## 🚀 راه‌اندازی

### اجرای سرور
```bash
python app.py
```

سرور روی `http://localhost:3000` اجرا خواهد شد.

## 📁 ساختار پروژه

```
soundcloud-music-streamer/
├── app.py              # فایل اصلی Flask
├── music_api.py        # API برای SoundCloud
├── requirements.txt    # پکیج‌های مورد نیاز
├── downloads/          # پوشه فایل‌های دانلود شده
├── templates/          # قالب‌های HTML
│   ├── index.html
│   └── player.html
└── static/            # فایل‌های CSS/JS
    ├── style.css
    └── script.js
```

## 🔧 استفاده

### 1. جستجوی موسیقی
- صفحه اصلی را باز کنید
- نام آهنگ یا هنرمند را وارد کنید
- روی "جستجو" کلیک کنید

### 2. پخش آنلاین
- روی دکمه "▶️ Play" کنار آهنگ مورد نظر کلیک کنید
- صفحه پخش باز شده و موسیقی شروع می‌شود

### 3. دانلود
- روی دکمه "📥 Download" کلیک کنید
- فایل در پوشه `downloads` ذخیره می‌شود

## 🌐 API Endpoints

```
GET  /                     # صفحه اصلی
POST /search               # جستجوی موسیقی
GET  /play/<track_id>      # پخش آهنگ
GET  /download/<track_id>  # دانلود آهنگ
GET  /downloads/<filename> # سرو فایل‌های دانلود شده
```

### مثال API:
```bash
# جستجو
curl -X POST http://localhost:3000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "eminem lose yourself"}'

# دانلود
curl http://localhost:3000/download/artist-name/track-name
```

## ⚙️ تنظیمات

### تغییر تعداد نتایج جستجو
در فایل `music_api.py`:
```python
# تغییر عدد 20 به تعداد دلخواه
search_results = ydl.extract_info(
    f"scsearch20:{song_name}",  # 20 را تغییر دهید
    download=False
)
```

### تغییر پورت سرور
در فایل `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=3000)  # پورت را تغییر دهید
```

## 🐛 عیب‌یابی

### مشکلات رایج:

1. **FFmpeg not found**
   - مطمئن شوید FFmpeg نصب شده و در PATH قرار دارد

2. **Permission denied در downloads**
   - مجوزهای پوشه downloads را بررسی کنید
   ```bash
   chmod 755 downloads/
   ```

3. **آهنگ فقط 30 ثانیه پخش می‌شود**
   - برخی آهنگ‌ها در SoundCloud فقط preview دارند
   - این محدودیت از سمت SoundCloud است

4. **جستجو کار نمی‌کند**
   - اتصال اینترنت را بررسی کنید
   - ممکن است SoundCloud دسترسی را محدود کرده باشد

## 📝 مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر فایل LICENSE را مطالعه کنید.

## 🤝 مشارکت

1. Fork کنید
2. Feature branch بسازید (`git checkout -b feature/AmazingFeature`)
3. تغییرات را commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. Branch را push کنید (`git push origin feature/AmazingFeature`)
5. Pull Request ایجاد کنید

## ⚠️ اخطار قانونی

این ابزار صرفاً برای اهداف آموزشی و شخصی طراحی شده است. لطفاً از قوانین کپی‌رایت پیروی کرده و فقط از موسیقی‌هایی استفاده کنید که مجوز دانلود آن‌ها را دارید.

## 📞 پشتیبانی

اگر مشکلی داشتید یا سوالی بود، در بخش Issues گیت‌هاب مطرح کنید.

---

**ساخته شده با ❤️ و Python**
