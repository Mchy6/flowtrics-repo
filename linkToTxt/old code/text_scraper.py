import requests
from bs4 import BeautifulSoup
import logging


def scrape_text(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            text = soup.get_text()

            return text

        else:
            logging.info(f"Webpage {url} inaccessible for text scraping. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(e)
