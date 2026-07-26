import yfinance as yf


class StockScreener:
    def __init__(self):
        pass

    def screen(self, symbols):
        results = []

        for symbol in symbols:
            try:
                stock = yf.Ticker(symbol)
                info = stock.info

                pe = info.get("trailingPE")
                roe = info.get("returnOnEquity")
                debt = info.get("debtToEquity")
                price = info.get("currentPrice")
                market_cap = info.get("marketCap")

                if (
                    pe
                    and roe
                    and debt is not None
                    and pe < 25
                    and roe > 0.15
                    and debt < 100
                ):
                    results.append(
                        {
                            "Symbol": symbol,
                            "Price": price,
                            "PE": pe,
                            "ROE": roe,
                            "Debt/Equity": debt,
                            "Market Cap": market_cap,
                        }
                    )

            except Exception:
                continue

        return results


if __name__ == "__main__":
    screener = StockScreener()

    stocks = [
        "AAPL",
        "MSFT",
        "GOOG",
        "META",
        "NVDA",
        "TSLA",
    ]

    results = screener.screen(stocks)

    for stock in results:
        print(stock)
