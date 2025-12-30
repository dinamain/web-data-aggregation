from scraper.base_scraper import BaseScraper

class BookScraper(BaseScraper):

    def scrape(self):
        url = self.base_url
        html = self.fetch_page(url)

        if not html:
            return []

        soup = self.parse_html(html)
        books = []

        book_blocks = soup.find_all("article", class_="product_pod")

        for book in book_blocks:
            title = book.h3.a["title"]
            price_text = book.find("p", class_="price_color").text

            books.append({
                "title": title,
                "price": price_text
            })

        return books
