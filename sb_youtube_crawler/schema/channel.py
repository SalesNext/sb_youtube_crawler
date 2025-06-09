from pydantic import BaseModel
from typing import Optional, List

class Channel(BaseModel):
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    channel_id_user: Optional[str] = None
    channel_title: Optional[str] = None
    channel_follower_count: Optional[str] = None
    channel_created_one: Optional[str] = None
    channel_view_count: Optional[str] = None
    channel_video_count: Optional[str] = None
    channel_rating_grade: Optional[str] = None
    channel_description: Optional[str] = None
    channel_sb_ranking: Optional[str] = None
    channel_subcriber_ranking: Optional[str] = None
    channel_views_ranking: Optional[str] = None
    channel_country_rank: Optional[str] = None
    channel_category_rank: Optional[str] = None
    channel_tags: Optional[List[str]] = None
    channel_uploader_id: Optional[str] = None
    channel_uploader_url: Optional[str] = None
    channel_playlist_count: Optional[int] = None
    source_channel_url: Optional[str] = None
    channel_release_year: Optional[int] = None
    