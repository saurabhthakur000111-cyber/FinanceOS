from financeos.market.market_data import MarketData


class FinancialAI:

    def __init__(self):
        self.market = MarketData()

    def analyze(self, symbol):

        stock = self.market.get_stock(symbol)

        price = stock["price"]
        previous = stock["previous_close"]

        if price > previous:
            signal = "BUY"
        elif price < previous:
            signal = "SELL"
        else:
            signal = "HOLD"

        print("========== AI ANALYSIS ==========")
        print("Company :", stock["name"])
        print("Price   :", price)
        print("Signal  :", signal)


if __name__ == "__main__":

    ai = FinancialAI()
    ai.analyze("AAPL")