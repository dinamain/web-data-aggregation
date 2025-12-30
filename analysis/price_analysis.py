import sqlite3
import pandas as pd

class PriceAnalyzer:
    def __init__(self, db_path="database/products.db"):
        self.db_path = db_path

    def load_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT * FROM products", conn)
        conn.close()
        return df

    def generate_insights(self, df):
        insights = {
            "total_products": len(df),
            "average_price": df["price"].mean(),
            "min_price": df["price"].min(),
            "max_price": df["price"].max()
        }
        return insights

    def export_csv(self, df):
        df.to_csv("data/processed/products.csv", index=False)
