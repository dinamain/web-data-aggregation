from scraper.base_scraper import BaseScraper

class BookScraper(BaseScraper):

    def scrape(self):
        current_url = self.base_url
        all_books = []
        visited_urls = set()

        while current_url:
            if current_url in visited_urls:
                break
            visited_urls.add(current_url)

            html = self.fetch_page(current_url)
            if not html:
                break

            soup = self.parse_html(html)

            # Extract books on current page
            book_blocks = soup.find_all("article", class_="product_pod")

            for book in book_blocks:
                title = book.h3.a["title"]
                price_text = book.find("p", class_="price_color").text

                all_books.append({
                    "title": title,
                    "price": price_text
                })

            # Find next page
            next_btn = soup.find("li", class_="next")
            if next_btn and next_btn.a:
                next_href = next_btn.a["href"]
                current_url = self._build_next_url(next_href)
            else:
                current_url = None

        return all_books

    def _build_next_url(self, next_href):
        if "catalogue" in self.base_url:
            return self.base_url.rsplit("/", 1)[0] + "/" + next_href
        else:
            return self.base_url + "catalogue/" + next_href
