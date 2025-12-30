from utils.logger import setup_logger
from scraper.site1_scraper import BookScraper
from cleaning.data_cleaner import DataCleaner
from database.data_store import DataStore
from analysis.price_analysis import PriceAnalyzer
setup_logger()

# 1. Scrape
scraper = BookScraper("https://books.toscrape.com/")
raw_data = scraper.scrape()
print(f"Raw records: {len(raw_data)}")

# 2. Clean
cleaner = DataCleaner()
cleaned_data = cleaner.clean_data(raw_data)
print(f"Cleaned records: {len(cleaned_data)}")

# 3. Store
store = DataStore()
store.create_table()
store.insert_records(cleaned_data)

print("Data successfully stored in SQLite database")

# 4. Analyze
analyzer = PriceAnalyzer()
df = analyzer.load_data()

insights = analyzer.generate_insights(df)
analyzer.export_csv(df)

print("Analysis Insights:")
for k, v in insights.items():
    print(f"{k}: {v}")