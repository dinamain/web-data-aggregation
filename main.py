from utils.logger import setup_logger
from utils.config_loader import load_site_config
from scraper.generic_scraper import GenericScraper
from cleaning.data_cleaner import DataCleaner
from database.data_store import DataStore
from analysis.price_analysis import PriceAnalyzer
from analysis.price_comparator import PriceComparator


def main():
    setup_logger()

    # 1. Load site configuration
    site_config = load_site_config("books")
    # site_config = load_site_config("quotes")

    # 2. Scrape
    scraper = GenericScraper(site_config)
    raw_data = scraper.scrape()
    print(f"Raw records: {len(raw_data)}")

    # 3. Clean
    cleaner = DataCleaner()
    cleaned_data = cleaner.clean_data(raw_data)
    print(f"Cleaned records: {len(cleaned_data)}")

    # 4. Initialize DB
    store = DataStore()
    store.create_table()
    store.create_price_history_table()

    # 5. Snapshot BEFORE update
    previous_prices = store.get_all_latest_prices()
    # format: {(source, title): price}

    comparator = PriceComparator()

    # 6. Compare against previous snapshot
    for record in cleaned_data:
        key = (record["source"], record["title"])
        old_price = previous_prices.get(key)
        new_price = record["price"]

        change = comparator.calculate_change(old_price, new_price)

        if change is not None:
            store.insert_price_change({
                "source": record["source"],
                "title": record["title"],
                "old_price": old_price,
                "new_price": new_price,
                "change_percent": change,
                "scraped_at": record["scraped_at"]
            })

    # 7. Update latest snapshot (UPSERT)
    store.insert_records(cleaned_data)
    print("Data successfully stored in SQLite database")

    # 8. Analysis
    analyzer = PriceAnalyzer()
    df = analyzer.load_data()
    insights = analyzer.generate_insights(df)

    print("Analysis Insights:")
    for k, v in insights.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
