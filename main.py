from utils.logger import setup_logger
from scraper.site1_scraper import BookScraper

setup_logger()

scraper = BookScraper("https://books.toscrape.com/")
data = scraper.scrape()

print(f"Total books scraped: {len(data)}")
print("Sample records:")
for item in data[:5]:
    print(item)
