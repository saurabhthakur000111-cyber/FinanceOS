import math


class BlackScholes:
    def __init__(self, stock_price, strike_price, time, rate, volatility):
        self.S = stock_price
        self.K = strike_price
        self.T = time
        self.r = rate
        self.sigma = volatility

    def _cdf(self, x):
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))

    def call_price(self):
        d1 = (math.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (
            self.sigma * math.sqrt(self.T)
        )

        d2 = d1 - self.sigma * math.sqrt(self.T)

        return self.S * self._cdf(d1) - self.K * math.exp(-self.r * self.T) * self._cdf(
            d2
        )

    def put_price(self):
        d1 = (math.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (
            self.sigma * math.sqrt(self.T)
        )

        d2 = d1 - self.sigma * math.sqrt(self.T)

        return self.K * math.exp(-self.r * self.T) * self._cdf(
            -d2
        ) - self.S * self._cdf(-d1)


if __name__ == "__main__":
    option = BlackScholes(
        stock_price=100,
        strike_price=100,
        time=1,
        rate=0.05,
        volatility=0.20,
    )

    print("Call Price :", round(option.call_price(), 2))
    print("Put Price  :", round(option.put_price(), 2))
