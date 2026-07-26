from financeos.valuation.dcf import DCFValuation
from financeos.valuation.graham import GrahamValuation


class CompanyValuation:

    def __init__(self):

        self.current_price = 333.02

    def show(self):

        dcf = DCFValuation(
            free_cash_flow=100,
            growth_rate=0.10,
            discount_rate=0.12,
            terminal_growth=0.03
        )

        dcf_value = dcf.calculate()

        graham = GrahamValuation(
            eps=12,
            book_value=45
        )

        graham_value = graham.calculate()

        intrinsic = (dcf_value + graham_value) / 2

        margin = (
            (intrinsic - self.current_price)
            / intrinsic
        ) * 100

        print("========== COMPANY VALUATION ==========")

        print(f"Current Price    : ₹{self.current_price:.2f}")
        print(f"DCF Value        : ₹{dcf_value:.2f}")
        print(f"Graham Value     : ₹{graham_value:.2f}")
        print(f"Intrinsic Value  : ₹{intrinsic:.2f}")
        print(f"Margin of Safety : {margin:.2f}%")

        if intrinsic > self.current_price:
            print("Recommendation   : BUY")
        else:
            print("Recommendation   : SELL")


if __name__ == "__main__":

    CompanyValuation().show()