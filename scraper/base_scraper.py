import requests
from bs4 import BeautifulSoup
import logging

class BaseScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"Failed to fetch {url}: {e}")
            return None

    def parse_html(self, html):
        return BeautifulSoup(html, "lxml")
