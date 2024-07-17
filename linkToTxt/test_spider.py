import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class LinkSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://en.wikipedia.org/wiki/Indian_peafowl",
    ]
    links = []

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        print(links)

        class TextSpider(scrapy.Spider):
            name = "text"
            start_urls = links

            def parse(self, response):
                text = response.css('p::text').getall()
                print(text)

        process = CrawlerProcess(get_project_settings())
        process.crawl(TextSpider)
        process.start()
