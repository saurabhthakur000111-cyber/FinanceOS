from financeos.market.market_data import MarketData


class FinancialAI:

    def __init__(self):
        self.market = MarketData()

    def analyze(self, symbol):

        stock = self.market.get_stock(symbol)

        price = stock["price"]

        if price > stock["previous_close"]:
            signal = "BUY"
        elif price < stock["previous_close"]:
            signal = "SELL"
        else:
            signal = "HOLD"

        print("========== AI ANALYSIS ==========")
        print(f"Company : {stock['name']}")
        print(f"Price   : {price}")
        print(f"Signal  : {signal}")


if __name__ == "__main__":

    ai = FinancialAI()

    ai.analyze("AAPL")
