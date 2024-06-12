import requests
from bs4 import BeautifulSoup
import re
import logging


def scrape_links(url: str) -> list[str]:

    try:
        response = requests.get(url)

        links: list[str] = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            anchor_tags = soup.find_all('a')
            links = [tag.get('href') for tag in anchor_tags if tag.get('href')]
        else:
            logging.info(f"Webpage {url} inaccessible for link scraping. Status code: {response.status_code}")

        valid_links = filter_valid_urls(links)
        return valid_links

    except requests.exceptions.RequestException as e:
        logging.error(e)

def filter_valid_urls(links):
    valid_urls = []
    for link in links:
        # Regular expression pattern to match valid URLs
        pattern = r'^(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(?:\/[a-zA-Z0-9-._?&=/]*)?$'
        if re.match(pattern, link):
            valid_urls.append(link)
    return valid_urls
