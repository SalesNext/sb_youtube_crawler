from collections.abc import Iterable
from salesnext_crawler.events import CrawlEvent, DataEvent, Event
from scrapy.http.response.html import HtmlResponse
from scrapy import Request
from sb_youtube_crawler.parser.parse_channel_detail import parse_channel_detail
from sb_youtube_crawler.parser.parse_video_list import parse_video_list
from sb_youtube_crawler.parser.parse_video_detail import parse_video_detail
from sb_youtube_crawler.schema.channel import Channel

def parse_channel(
    event: CrawlEvent[None, Event, HtmlResponse],
    response: HtmlResponse,
) -> Iterable[Event]:
    channel_url = ''
    getlink = response.xpath("//a[@target='_blank']/@href").getall()
    for link in getlink:
        if 'channel' in link:
            channel_url = link
            break
    channel = Channel(
    channel_id_user = response.xpath("//span[@class='text-sm font-normal opacity-90']/text()").get(),
    channel_name = response.xpath("//span[@class='truncate max-w-full']/text()").get(),
    channel_follower_count = response.xpath('//p[contains(text(), "subscribers")]/parent::div/p[2]/text()').get(),
    channel_created_on = response.xpath('//p[contains(text(), "Created On")]/parent::div/p[2]/text()').get(),
    channel_view_count = response.xpath('//p[contains(text(), "views")]/parent::div/p[2]/text()').get(),
    channel_video_count = response.xpath('//p[contains(text(), "videos")]/parent::div/p[2]/text()').get(),
    channel_rating_grade = response.xpath('//h4[text()="Grade"]/preceding-sibling::h2[1]/text()').get(),
    
    channel_sb_ranking= response.xpath("//h2[@class='text-3xl font-bold']/text()").getall()[-5],
    channel_subcriber_ranking= response.xpath("//h2[@class='text-3xl font-bold']/text()").getall()[-4],
    channel_views_ranking = response.xpath("//h2[@class='text-3xl font-bold']/text()").getall()[-3],
    channel_country_rank = response.xpath("//h2[@class='text-3xl font-bold']/text()").getall()[-2],
    channel_category_rank = response.xpath("//h2[@class='text-3xl font-bold']/text()").getall()[-1],
    )
    channel_extra = parse_channel_detail(f'https://youtube.com/{channel.channel_id_user}')
    
    full_data_channel = channel.model_copy(update=channel_extra.model_dump(exclude_unset=True))
    yield DataEvent("channel", full_data_channel)
    
    videos = parse_video_list(f'https://youtube.com/{channel.channel_id_user}')
    for video in videos:
        video_detail = parse_video_detail(video)
        yield DataEvent("video", video_detail)
        
    