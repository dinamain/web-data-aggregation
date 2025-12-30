from utils.logger import setup_logger
from scraper.site1_scraper import BookScraper
from cleaning.data_cleaner import DataCleaner

setup_logger()

# Scraping
scraper = BookScraper("https://books.toscrape.com/")
raw_data = scraper.scrape()

print(f"Raw records: {len(raw_data)}")

# Cleaning
cleaner = DataCleaner()
cleaned_data = cleaner.clean_data(raw_data)

print(f"Cleaned records: {len(cleaned_data)}")

# Show sample
for item in cleaned_data[:5]:
    print(item)
