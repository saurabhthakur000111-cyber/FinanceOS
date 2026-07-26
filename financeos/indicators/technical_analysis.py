import yfinance as yf


class TechnicalAnalysis:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_price(self):
        stock = yf.Ticker(self.symbol)
        data = stock.history(period="5d")

        closes = list(data["Close"])

        current = closes[-1]
        average = sum(closes) / len(closes)

        print("========== TECHNICAL ANALYSIS ==========")
        print("Company :", self.symbol)
        print("Current Price :", round(current, 2))
        print("5-Day Average :", round(average, 2))

        if current > average:
            print("Trend : BULLISH")
        else:
            print("Trend : BEARISH")


if __name__ == "__main__":
    ta = TechnicalAnalysis("AAPL")
    ta.get_price()