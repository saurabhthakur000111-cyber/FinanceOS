from financeos.database.database import Database


class DataLoader:

    def __init__(self):
        self.db = Database()

    def get_stocks(self):
        query = """
        SELECT symbol, price, volume, created_at
        FROM stocks
        """

        return self.db.fetch_all(query)


if __name__ == "__main__":

    loader = DataLoader()

    stocks = loader.get_stocks()

    print("========== STOCK DATA ==========")

    for stock in stocks:
        print(stock)
