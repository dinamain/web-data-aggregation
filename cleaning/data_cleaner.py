import re
from datetime import datetime
import logging

class DataCleaner:

    def clean_price(self, price_str):
        """
        Converts price string like '£51.77' to float 51.77
        """
        if not price_str:
            return None

        try:
            price = re.sub(r"[^\d.]", "", price_str)
            return float(price)
        except Exception as e:
            logging.error(f"Price cleaning failed: {price_str} | {e}")
            return None

    def detect_currency(self, price_str):
        """
        Detect currency symbol
        """
        if not price_str:
            return None

        if "£" in price_str:
            return "GBP"
        if "$" in price_str:
            return "USD"
        if "₹" in price_str:
            return "INR"

        return "UNKNOWN"

    def clean_record(self, record):
        """
        Cleans a single scraped record
        """
        cleaned = {
            "title": record.get("title"),
            "price": self.clean_price(record.get("price")),
            "currency": self.detect_currency(record.get("price")),
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return cleaned

    def clean_data(self, raw_data):
        """
        Cleans list of raw records
        """
        cleaned_data = []

        for record in raw_data:
            if not record.get("title"):
                continue  # Skip invalid records

            cleaned_data.append(self.clean_record(record))

        return cleaned_data
