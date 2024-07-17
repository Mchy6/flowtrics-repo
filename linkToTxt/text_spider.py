import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup
from scrapy import signals
from collections import defaultdict


class TextExtractorSpider(scrapy.Spider):
    name = 'text_extractor'

    def __init__(self, urls=None, *args, **kwargs):
        super(TextExtractorSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls or []

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        yield {response.url: text}


def scrape_text_from_urls(urls):
    results = defaultdict(str)

    def crawler_results(signal, sender, item, response, spider):
        results.update(item)

    process = CrawlerProcess(get_project_settings())

    crawler = process.create_crawler(TextExtractorSpider)
    crawler.signals.connect(crawler_results, signal=signals.item_scraped)

    process.crawl(crawler, urls=urls)
    process.start()

    return dict(results)
