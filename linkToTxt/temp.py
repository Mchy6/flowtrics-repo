import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup
from scrapy import signals
from collections import defaultdict
from url import URL
import logging
import os


class TextExtractorSpider(scrapy.Spider):
    name = 'text_extractor'

    def __init__(self, urls=None, *args, **kwargs):
        super(TextExtractorSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls or []

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Clean up text files directory
    for file in os.listdir('text files'):
        full_path = os.path.join('text files', file)
        os.remove(full_path)

    url = URL('https://flowtrics.com/')
    url = URL('https://en.wikipedia.org/wiki/Indian_peafowl')

    links = url.get_links()

    urls_to_scrape = links

    result_dict = scrape_text_from_urls(urls_to_scrape)

    for url, text in result_dict.items():
        print("hi")
        print(f"URL: {url}")
        print(f"Text (first 100 characters): {text[:100]}...")
        print("-" * 50)

