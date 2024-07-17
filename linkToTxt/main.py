from text_spider import scrape_text_from_urls
import os
import logging
from link_scraper import scrape_links


def url_get_simple_name(long_url: str) -> str:
    return long_url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", ".")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info(f"Current working directory: {os.getcwd()}")

    # Clean up text files directory
    for file in os.listdir('text files'):
        full_path = os.path.join('text files', file)
        os.remove(full_path)
        logging.info(f"Deleted file: {full_path}")

    url = input("Enter a URL: ")

    if not url.startswith('http'):
        url = 'https://' + url

    logging.info(f"Scraping links from URL: {url}")

    urls_to_scrape = scrape_links(url)
    logging.info(f"Found {len(urls_to_scrape)} URLs to scrape")

    result_dict = scrape_text_from_urls(urls_to_scrape)
    logging.info(f"Scraped text from {len(result_dict)} URLs")

    for url, text in result_dict.items():
        file_name = f'text files/{url_get_simple_name(url)}.txt'
        with open(file_name, 'w') as new_file:
            new_file.write(f'Scraped from URL: {url}\n\n----------\n\n{text}')

        logging.info(f"Written scraped text to {file_name}")
