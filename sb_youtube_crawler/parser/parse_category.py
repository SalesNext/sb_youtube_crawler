from collections.abc import Iterable
from sb_youtube_crawler.parser.parse_channel import parse_channel
from salesnext_crawler.events import CrawlEvent, DataEvent, Event
from scrapy.http.response.html import HtmlResponse
from scrapy import Request


def parse_category(
    event: CrawlEvent[None, Event, HtmlResponse],
    response: HtmlResponse,
) -> Iterable[Event]:
    
    
    urls = response.xpath("//a[@class='block']/@href").getall()
    urls = list(set(urls))
    for url in urls[:2]:
        yield CrawlEvent(
            request= Request(url=response.urljoin(url)),
            metadata= None,
            callback = parse_channel,
        )