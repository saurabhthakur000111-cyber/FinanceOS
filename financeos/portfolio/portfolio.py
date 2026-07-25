class Portfolio:

    def __init__(self):
        self.assets = []

    def add_asset(self, symbol, shares, price):
        self.assets.append({
            "symbol": symbol,
            "shares": shares,
            "price": price
        })

    def total_value(self):
        total = 0

        for asset in self.assets:
            total += asset["shares"] * asset["price"]

        return total

    def show(self):
        print("========== PORTFOLIO ==========")

        for asset in self.assets:
            value = asset["shares"] * asset["price"]

            print(
                f'{asset["symbol"]} | '
                f'{asset["shares"]} shares | '
                f'₹{asset["price"]:.2f} | '
                f'Value = ₹{value:.2f}'
            )

        print("----------------------------")
        print(f"Total Portfolio Value : ₹{self.total_value():,.2f}")


if __name__ == "__main__":

    p = Portfolio()

    p.add_asset("AAPL", 10, 333.02)
    p.add_asset("MSFT", 5, 520.40)
    p.add_asset("GOOG", 3, 205.80)

    p.show()