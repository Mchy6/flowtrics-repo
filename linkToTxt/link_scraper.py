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
    pattern = (
        r'^(https?:\/\/)?'  # match the scheme (http or https)
        r'(?:www\.)?'  # optionally match www
        r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.'  # match the domain name part
        r'[a-zA-Z]{2,6}'  # match the top-level domain (e.g., com, net, org)
        r'(\/[-a-zA-Z0-9@:%._\+~#=\/]*)?'  # match the rest of the URL path
        r'(?![^\/]*(?:\.(?:pdf|docx?|txt|rtf|odt|jpg|jpeg|png|gif|bmp|tiff|svg|'
        r'mp3|wav|aac|flac|ogg|mp4|avi|mkv|mov|wmv|zip|rar|7z|tar|gz|'
        r'exe|bat|sh|bin|msi|html?|css|js|php|xml|xls|xlsx|ods|csv|'
        r'ppt|pptx|odp|db|sql|mdb|accdb|py|java|c|cpp)))'
    )

    for link in links:
        if re.match(pattern, link):
            valid_urls.append(link)

    return valid_urls
