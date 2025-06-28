from flask import Flask, render_template, request, jsonify, send_from_directory
import yt_dlp
import os
from music_api import search_song, get_audio_url

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        query = request.json.get('query', '')
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        
        results = search_song(query)
        if not results:
            return jsonify({'error': 'No results found'}), 404
        
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/play/<path:track_id>')
def play(track_id):
    try:
        audio_url = get_audio_url(track_id)
        if not audio_url:
            return jsonify({'error': 'Audio not found'}), 404
        
        return render_template('player.html', 
                             track_id=track_id, 
                             audio_url=audio_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<path:track_id>')
def download(track_id):
    try:
        ydl_opts = {
            'format': 'bestaudio[ext!=webm]/best[ext!=webm]/bestaudio/best',
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
            'extractaudio': True,
            'audioformat': 'mp3',
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
            
            ydl.download([url])
        
        return jsonify({'status': 'downloaded'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/downloads/<filename>')
def serve_download(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)