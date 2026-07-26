class DCFValuation:

    def __init__(self, free_cash_flow, growth_rate,
                 discount_rate, terminal_growth):

        self.fcf = free_cash_flow
        self.growth = growth_rate
        self.discount = discount_rate
        self.terminal = terminal_growth

    def calculate(self):

        value = 0

        cashflow = self.fcf

        for year in range(1, 6):

            cashflow *= (1 + self.growth)

            value += cashflow / ((1 + self.discount) ** year)

        terminal_value = (
            cashflow * (1 + self.terminal)
        ) / (self.discount - self.terminal)

        terminal_value /= ((1 + self.discount) ** 5)

        value += terminal_value

        return value


if __name__ == "__main__":

    dcf = DCFValuation(
        free_cash_flow=100,
        growth_rate=0.10,
        discount_rate=0.12,
        terminal_growth=0.03
    )

    print("DCF Value =", round(dcf.calculate(), 2))