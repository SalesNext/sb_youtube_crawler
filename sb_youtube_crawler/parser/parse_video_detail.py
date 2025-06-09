from yt_dlp import YoutubeDL
from typing import Dict
from sb_youtube_crawler.schema.video import Video

def parse_video_detail(video_url: str) -> Dict:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        
        video = Video(
            video_id = info.get("id"),
            video_title = info.get("fulltitle"),
            video_description = info.get("description"),
            video_thumbnail = info.get("thumbnail"),
            video_channel_id = info.get("channel_id"),
            video_channel_url = info.get("channel_url"),
            video_view_count = info.get("view_count"),
            video_average_rating = info.get("average_rating"),
            video_age_limit = info.get("age_limit"),
            source_video_url = info.get("webpage_url"),
            video_category = info.get("categories"),
            video_tags = info.get("tags"),
            video_media_type = info.get("media_type"),
            video_release_date = info.get("release_timestamp"),
            video_comment_count= info.get("comment_count"),
            video_like_count = info.get("like_count"),
            video_channel_name = info.get("uploader"),
            video_uploader_id= info.get("uploader_id"),
            video_uploader_url = info.get("uploader_url"),
            video_privacy_status = info.get("privacy_status"),
            video_release_year = info.get("release_year"),
            video_language = info.get("language"),
            video_quality_rate = info.get("quality"),
            
        )

    return video
