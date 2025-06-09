from yt_dlp import YoutubeDL
from sb_youtube_crawler.schema.channel import Channel
def parse_channel_detail(channel_url):    
  

    ydl_opts = {
        'playlist_items': '1',
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
       
        channel = Channel(
            channel_id = info.get("id"),
            channel_title = info.get("title"),
            channel_description = info.get("description"),
            channel_tags = info.get("tags"),
            channel_uploader_id = info.get("uploader_id"),
            channel_uploader_url= info.get("uploader_url"),
            channel_playlist_count = info.get("playlist_count"),
            source_channel_url = info.get("webpage_url"),
            channel_realease_year = info.get("release_year")
        )
        
        return channel

    
