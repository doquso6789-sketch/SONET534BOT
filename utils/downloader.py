import os
import yt_dlp
from config import DOWNLOAD_DIR

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

YDL_OPTIONS = {
    "outtmpl": f"{DOWNLOAD_DIR}/%(title).80s.%(ext)s",
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "quiet": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "geo_bypass": True,
    "extract_flat": False,
    "cookiefile": "cookies.txt",
    "extractor_args": {
        "tiktok": {
            "api_hostname": "api16-normal-c-useast1a.tiktokv.com"
        }
    }
}


def download_video(url):
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=True)

        if not info:
            return None

        path = ydl.prepare_filename(info)

        if os.path.exists(path):
            return path

        base = os.path.splitext(path)[0]

        for ext in ["mp4", "mkv", "webm", "mp3", "m4a"]:
            alt = f"{base}.{ext}"

            if os.path.exists(alt):
                return alt

    return None
