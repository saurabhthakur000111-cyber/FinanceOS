import yfinance as yf

from financeos.database import Database


class LiveDataLoader:

    def __init__(self):
        self.db = Database()

    def fetch_stock(self, symbol):

        stock = yf.Ticker(symbol)
        info = stock.info

        price = info.get("currentPrice")
        volume = info.get("volume")

        print(f"Saving {symbol}...")
        print(f"Price : {price}")
        print(f"Volume: {volume}")

        self.db.save_stock(
            symbol,
            price,
            volume
        )


if __name__ == "__main__":

    loader = LiveDataLoader()

    loader.fetch_stock("AAPL")
    loader.fetch_stock("MSFT")
    loader.fetch_stock("GOOG")

    print("\nLive data saved successfully.")