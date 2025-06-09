from collections.abc import Iterable
from salesnext_crawler.crawler import ScrapyCrawler
from salesnext_crawler.events import CrawlEvent, Event, SitemapEvent
from scrapy import Request
import pyarrow as pa
from sb_youtube_crawler.parser.parse_category import parse_category


class SbYoutubeCrawler(ScrapyCrawler):
    def __init__(self, daily: bool = False
                 ) -> None:
        self.daily = daily
    def start(self) -> Iterable[Event]: 
        
        categories = [
            'games',
            'entertainment',
            'people',
            'animals',
            'film',
            'music',
            'sports',
            'tech',
            'howto',
            'news',
            'education',
            'comedy',
            'nonprofit',
            'autos',
            'travel',      
        ]
        
        for category in categories:            
            yield CrawlEvent(
        request = Request(f'https://socialblade.com/youtube/lists/top/100/sb/{category}/JP'),
        metadata= None,
        callback= parse_category,
    )
            
            
         

    