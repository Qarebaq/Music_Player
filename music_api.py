import yt_dlp
import requests
import re

def search_song(song_name):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(
                f"scsearch20:{song_name}",
                download=False
            )
            
            if not search_results or 'entries' not in search_results:
                return None
            
            results = []
            for entry in search_results['entries']:
                # استخراج کامل URL بدون تغییر برای track_id
                url = entry.get('url', '') or entry.get('webpage_url', '')
                if url and 'soundcloud.com' in url:
                    results.append({
                        'videoId': url,  # کامل URL را به عنوان track_id استفاده می‌کنیم
                        'title': entry.get('title', 'Unknown'),
                        'artists': [{'name': entry.get('uploader', 'Unknown Artist')}],
                        'duration': entry.get('duration', 0),
                        'thumbnails': entry.get('thumbnails', [])
                    })
            
            return results[:20] if results else None
            
    except Exception as e:
        print(f"Search error: {e}")
        return None

def get_audio_url(track_id):
    try:
        ydl_opts = {
            'format': 'bestaudio[ext!=webm]/best[ext!=webm]/bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'extractaudio': True,
            'prefer_free_formats': False,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                'Keep-Alive': '300',
                'Connection': 'keep-alive',
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # اگر track_id شامل https نباشد، آن را اضافه کن
            if not track_id.startswith('http'):
                url = f"https://soundcloud.com/{track_id}"
            else:
                url = track_id
            
            info = ydl.extract_info(url, download=False)
            
            # سعی می‌کنیم بهترین کیفیت را پیدا کنیم که preview نباشد
            formats = info.get('formats', [])
            
            # اولویت: progressive formats که معمولاً کامل هستند
            for fmt in formats:
                if fmt.get('vcodec') == 'none' and fmt.get('acodec') != 'none':
                    if fmt.get('protocol') in ['https', 'http']:
                        duration = fmt.get('duration') or info.get('duration')
                        if duration and duration > 60:  # اگر بیشتر از ۶۰ ثانیه باشد
                            return fmt.get('url')
            
            # اگر پیدا نشد، URL اصلی را برگردان
            return info.get('url')
            
    except Exception as e:
        print(f"URL extraction error: {e}")
        return None