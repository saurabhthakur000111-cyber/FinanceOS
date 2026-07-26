import yfinance as yf


class MarketData:

    def get_stock(self, symbol):

        stock = yf.Ticker(symbol)

        info = stock.info

        return {
            "symbol": symbol,
            "name": info.get("longName"),
            "price": info.get("currentPrice"),
            "previous_close": info.get("previousClose"),
            "market_cap": info.get("marketCap"),
            "volume": info.get("volume"),
        }


if __name__ == "__main__":

    market = MarketData()

    stock = market.get_stock("AAPL")

    print("========== LIVE STOCK DATA ==========")

    for key, value in stock.items():
        print(f"{key} : {value}")
