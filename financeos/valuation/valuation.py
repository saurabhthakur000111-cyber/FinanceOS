"""
FinanceOS Valuation Engine
Basic DCF valuation module
"""

class Valuation:

    def __init__(self, cash_flow, growth_rate, discount_rate):
        self.cash_flow = cash_flow
        self.growth_rate = growth_rate
        self.discount_rate = discount_rate


    def dcf_value(self, years=5):

        value = 0

        for year in range(1, years + 1):
            future_cash_flow = (
                self.cash_flow *
                ((1 + self.growth_rate) ** year)
            )

            discounted = (
                future_cash_flow /
                ((1 + self.discount_rate) ** year)
            )

            value += discounted

        return round(value, 2)


if __name__ == "__main__":

    valuation = Valuation(
        cash_flow=1000000,
        growth_rate=0.08,
        discount_rate=0.10
    )

    result = valuation.dcf_value()

    print("========== DCF VALUATION ==========")
    print("Intrinsic Value :", result)