from yt_dlp import YoutubeDL


ydl_opts = {
    'format_sort': ['res:1080', 'ext:mp4:m4a'],
    'outtmpl': f'vid/%(title)s.%(ext)s',
}

URLS = ["https://www.youtube.com/watch?v=qMl7G4Jcw6c"]

# Download subtitles
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)

