import os
import yt_dlp

from config import DOWNLOAD_DIR

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def get_ydl_options(url):

    # SOUNDCLOUD / AUDIO
    if "soundcloud.com" in url or "music.youtube.com" in url:

        return {
            "outtmpl": f"{DOWNLOAD_DIR}/%(title).80s.%(ext)s",
            "format": "bestaudio/best",
            "quiet": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "ignoreerrors": True,

            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
        }

    # YOUTUBE VIDEO
    elif "youtube.com" in url or "youtu.be" in url:

        return {
            "outtmpl": f"{DOWNLOAD_DIR}/%(title).80s.%(ext)s",

            "format": (
                "bestvideo[ext=mp4]+bestaudio[ext=m4a]/"
                "best[ext=mp4]/best"
            ),

            "merge_output_format": "mp4",

            "quiet": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "ignoreerrors": True,
        }

    # DEFAULT SOCIAL
    else:

        return {
            "outtmpl": f"{DOWNLOAD_DIR}/%(title).80s.%(ext)s",

            "format": "bestvideo+bestaudio/best",

            "merge_output_format": "mp4",

            "quiet": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "ignoreerrors": True,
            "geo_bypass": True,

            "extractor_args": {
                "tiktok": {
                    "api_hostname":
                    "api16-normal-c-useast1a.tiktokv.com"
                }
            }
        }


def download_video(url):

    ydl_opts = get_ydl_options(url)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)

        if not info:
            return None

        path = ydl.prepare_filename(info)

        # CHECK DIRECT
        if os.path.exists(path):
            return path

        # CHECK OTHER EXTENSIONS
        base = os.path.splitext(path)[0]

        for ext in [
            "mp4",
            "mkv",
            "webm",
            "mp3",
            "m4a"
        ]:

            alt = f"{base}.{ext}"

            if os.path.exists(alt):
                return alt

    return None
