from scraper.base_scraper import BaseScraper
from urllib.parse import urljoin

class BookScraper(BaseScraper):

    def scrape(self):
        current_url = self.base_url
        all_books = []

        while current_url:
            print(f"Scraping: {current_url}")

            html = self.fetch_page(current_url)
            if not html:
                break

            soup = self.parse_html(html)

            # Extract books
            book_blocks = soup.find_all("article", class_="product_pod")

            for book in book_blocks:
                title = book.h3.a["title"]
                price_text = book.find("p", class_="price_color").text

                all_books.append({
                    "title": title,
                    "price": price_text
                })

            # Find next page
            next_btn = soup.select_one("li.next a")
            if next_btn:
                current_url = urljoin(current_url, next_btn["href"])
            else:
                break

        return all_books
