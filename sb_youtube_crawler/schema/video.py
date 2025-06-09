from pydantic import BaseModel
from typing import Optional, List

class Video(BaseModel):
    video_id: Optional[str] = None
    video_title: Optional[str] = None
    video_description: Optional[str] = None
    video_thumbnail: Optional[str] = None
    video_channel_id: Optional[str] = None
    video_channel_url: Optional[str] = None
    video_view_count: Optional[int] = None
    video_average_rating: Optional[float] = None
    video_age_limit: Optional[int] = None
    source_video_url: Optional[str] = None
    video_category: Optional[List[str]] = None
    video_tags: Optional[List[str]] = None
    video_media_type: Optional[str] = None
    video_release_date: Optional[int] = None
    video_comment_count: Optional[int] = None
    video_like_count: Optional[int] = None
    video_channel_name: Optional[str] = None
    video_uploader_id: Optional[str] = None
    video_uploader_url: Optional[str] = None 
    video_privacy_status: Optional[str] = None
    video_release_year: Optional[int] = None
    video_language: Optional[str] = None
    video_quality_rate: Optional[float] = None