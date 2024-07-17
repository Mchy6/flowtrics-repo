from url import URL
import os
import logging
import test_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from test_spider import LinkSpider

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    # Clean up text files directory
    for file in os.listdir('text files'):
        full_path = os.path.join('text files', file)
        os.remove(full_path)

    url = URL('https://flowtrics.com/')

    links = url.get_links()

    for link in links:
        print(link)
