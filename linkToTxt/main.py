from text_spider import scrape_text_from_urls
import os
import logging
from link_scraper import scrape_links


def url_get_simple_name(long_url: str) -> str:
    return long_url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", ".")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Clean up text files directory
    for file in os.listdir('text files'):
        full_path = os.path.join('text files', file)
        os.remove(full_path)

    url = 'https://flowtrics.com/'

    urls_to_scrape = scrape_links(url)

    result_dict = scrape_text_from_urls(urls_to_scrape)

    for url, text in result_dict.items():
        new_file = open(f'text files/{url_get_simple_name(url)}.txt', 'w')
        new_file.write(f'Scraped from URL: {url}\n\n----------\n\n{text}')
