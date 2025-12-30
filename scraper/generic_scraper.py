import yaml
from urllib.parse import urljoin
from scraper.base_scraper import BaseScraper

class GenericScraper(BaseScraper):
    def __init__(self, site_config):
        super().__init__(site_config["base_url"])
        self.config = site_config

    def scrape(self):
        current_url = self.base_url
        all_items = []

        while current_url:
            html = self.fetch_page(current_url)
            if not html:
                break

            soup = self.parse_html(html)

            products = soup.select(self.config["product_container"])

            for product in products:
                title_elem = product.select_one(self.config["title_selector"])
                price_elem = product.select_one(self.config["price_selector"])

                if not title_elem or not price_elem:
                    continue
                title_attr = self.config.get("title_attr")
                title_attr = self.config.get("title_attr")
                if title_attr:
                    title = title_elem.get(title_attr)
                else:
                    title = title_elem.text.strip()


                # title = title_elem.get(self.config["title_attr"])
                price = price_elem.text

                all_items.append({
                    "title": title,
                    "price": price
                })

            next_btn = soup.select_one(self.config["pagination"]["next_selector"])
            if next_btn:
                current_url = urljoin(current_url, next_btn["href"])
            else:
                break

        return all_items
