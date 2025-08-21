import yt_dlp


def extract_video_info(url: str) -> dict:
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "force_generic_extractor": False,
        "nocheckcertificate": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        # Fallback for URL extraction
        formats = info.get("formats", [])
        best = max(formats, key=lambda f: f.get("height", 0), default={})

        return {
            "title": info.get("title"),
            "uploader": info.get("uploader") or info.get("channel"),
            "duration": info.get("duration"),
            # "thumbnail": info.get("thumbnail"),
            "video_url": best.get("url"),
        }
