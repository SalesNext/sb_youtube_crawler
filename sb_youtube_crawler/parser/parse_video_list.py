from yt_dlp import YoutubeDL
from typing import List, Dict

def parse_video_list(channel_url: str) -> List[Dict]:
    ydl_opts = {
        'quiet': False,
    'skip_download': True,
    'extract_flat': True,
    'force_ipv4': True,
    'retries': 1,
    'fragment_retries': 1,
    'socket_timeout': 5,
    'concurrent_fragment_downloads': 10,
    'n_threads': 4,
    'ignoreerrors': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        channel_info = ydl.extract_info(channel_url, download=False)
        channel_id = channel_info.get("channel_id") or channel_info.get("id")

        uploads_playlist = f"https://www.youtube.com/playlist?list=UU{channel_id[2:]}"
        playlist_info = ydl.extract_info(uploads_playlist, download=False)

        entries = playlist_info.get("entries", [])
        videos = []

        for video in entries:
            video_id_list = video.get("id")
            video_url = f"https://www.youtube.com/watch?v={video_id_list}"
            videos.append(video_url)
           

        return videos
