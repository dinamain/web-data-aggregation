import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


class PriceVisualizer:
    def __init__(self, db_path="database/products.db"):
        self.db_path = db_path

    def load_products(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT title, price FROM products", conn)
        conn.close()
        return df

    def load_price_history(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("""
            SELECT title, old_price, new_price, scraped_at
            FROM price_history
        """, conn)
        conn.close()
        return df

    def plot_price_distribution(self, df):
        df = df.dropna(subset=["price"])

        plt.figure()
        plt.hist(df["price"], bins=20)
        plt.xlabel("Price")
        plt.ylabel("Number of Products")
        plt.title("Product Price Distribution")
        plt.show()

    def plot_top_expensive(self, df, top_n=10):
        df = df.dropna(subset=["price"])
        top = df.sort_values(by="price", ascending=False).head(top_n)

        plt.figure()
        plt.barh(top["title"], top["price"])
        plt.xlabel("Price")
        plt.ylabel("Product")
        plt.title(f"Top {top_n} Most Expensive Products")
        plt.gca().invert_yaxis()
        plt.show()

    def plot_price_changes(self, history_df):
        if history_df.empty:
            print("No price history data available")
            return

        history_df["scraped_at"] = pd.to_datetime(history_df["scraped_at"])

        plt.figure()
        plt.plot(history_df["scraped_at"], history_df["new_price"], marker="o")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Price Change Over Time")
        plt.show()
