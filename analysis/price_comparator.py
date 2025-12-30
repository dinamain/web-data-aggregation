class PriceComparator:

    def calculate_change(self, old_price, new_price, tolerance=0.01):
        if old_price is None or new_price is None:
            return None

        # Ignore tiny float differences
        if abs(old_price - new_price) < tolerance:
            return None

        try:
            return ((new_price - old_price) / old_price) * 100
        except ZeroDivisionError:
            return None
