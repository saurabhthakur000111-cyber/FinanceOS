class Portfolio:

    def __init__(self):
        self.assets = []

    def add_asset(self, symbol, shares, price):
        self.assets.append({"symbol": symbol, "shares": shares, "price": price})

    def total_value(self):
        total = 0

        for asset in self.assets:
            total += asset["shares"] * asset["price"]

        return total

    def show_portfolio(self):

        # Add sample data if portfolio is empty
        if not self.assets:
            self.add_asset("AAPL", 10, 333.02)
            self.add_asset("MSFT", 5, 381.70)
            self.add_asset("GOOG", 3, 319.09)

        print("========== PORTFOLIO ==========")

        for asset in self.assets:
            value = asset["shares"] * asset["price"]

            print(
                f'{asset["symbol"]} | '
                f'{asset["shares"]} Shares | '
                f'₹{asset["price"]:.2f} | '
                f"Value = ₹{value:.2f}"
            )

        print("------------------------------")
        print(f"Total Portfolio Value : ₹{self.total_value():,.2f}")

    # Backward compatibility
    def show(self):
        self.show_portfolio()


if __name__ == "__main__":

    portfolio = Portfolio()
    portfolio.show_portfolio()
