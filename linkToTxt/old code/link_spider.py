import scrapy
from scrapy.crawler import CrawlerProcess
import re

class LinkSpider(scrapy.Spider):
    name = "link"

    def __init__(self, start_url, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]


def run_link_spider(url) -> list[str]:
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    })

    result = []

    class ResultSpider(LinkSpider):
        def parse(self, response):
            for link in response.css('a::attr(href)').getall():
                result.append(link)

    process.crawl(ResultSpider, start_url=url)
    process.start()

    filtered_result = filter_valid_urls(result)

    return filtered_result


def filter_valid_urls(links):
    valid_urls = []
    for link in links:
        # Regular expression pattern to match valid URLs
        pattern = r'^(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(?:\/[a-zA-Z0-9-._?&=/]*)?$'
        if re.match(pattern, link):
            valid_urls.append(link)
    return valid_urls