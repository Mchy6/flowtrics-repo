from link_scraper import scrape_links
from text_scraper import scrape_text
import logging


class URL:
    def __init__(self, url: str):
        self.url: str = url
        self.name: str = self._get_name()

    def __str__(self) -> str:
        return self.url

    def get_links(self) -> list[str]:
        return scrape_links(self.url)

    def convert_to_txt(self) -> None:
        filename = f'text files/{self.name}.txt'
        text: str = scrape_text(self.url)

        if text is not None:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(scrape_text(self.url))
        else:
            logging.info(f"Failed to write text to file: {filename}, text is None.")

    def _get_name(self):
        return self.url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", ".")



