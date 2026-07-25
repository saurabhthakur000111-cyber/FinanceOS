class RatioAnalysis:

    def __init__(
        self,
        current_assets,
        current_liabilities,
        total_debt,
        total_equity,
        net_income,
        total_assets,
        revenue,
        gross_profit,
        shares_outstanding,
        market_price
    ):

        self.current_assets = current_assets
        self.current_liabilities = current_liabilities
        self.total_debt = total_debt
        self.total_equity = total_equity
        self.net_income = net_income
        self.total_assets = total_assets
        self.revenue = revenue
        self.gross_profit = gross_profit
        self.shares_outstanding = shares_outstanding
        self.market_price = market_price

    def current_ratio(self):
        return self.current_assets / self.current_liabilities

    def debt_to_equity(self):
        return self.total_debt / self.total_equity

    def roe(self):
        return self.net_income / self.total_equity

    def roa(self):
        return self.net_income / self.total_assets

    def gross_margin(self):
        return self.gross_profit / self.revenue

    def net_margin(self):
        return self.net_income / self.revenue

    def eps(self):
        return self.net_income / self.shares_outstanding

    def pe_ratio(self):
        return self.market_price / self.eps()


if __name__ == "__main__":

    ratio = RatioAnalysis(
        current_assets=500000,
        current_liabilities=250000,
        total_debt=400000,
        total_equity=600000,
        net_income=120000,
        total_assets=1000000,
        revenue=800000,
        gross_profit=320000,
        shares_outstanding=10000,
        market_price=333.02
    )

    print("========== FINANCIAL RATIOS ==========")
    print(f"Current Ratio : {ratio.current_ratio():.2f}")
    print(f"Debt/Equity   : {ratio.debt_to_equity():.2f}")
    print(f"ROE           : {ratio.roe():.2%}")
    print(f"ROA           : {ratio.roa():.2%}")
    print(f"Gross Margin  : {ratio.gross_margin():.2%}")
    print(f"Net Margin    : {ratio.net_margin():.2%}")
    print(f"EPS           : ₹{ratio.eps():.2f}")
    print(f"P/E Ratio     : {ratio.pe_ratio():.2f}")