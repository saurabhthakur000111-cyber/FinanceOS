import numpy as np


class MonteCarloSimulation:
    def __init__(
        self,
        initial_investment: float,
        expected_return: float,
        volatility: float,
        years: int,
        simulations: int = 1000,
    ):
        self.initial_investment = initial_investment
        self.expected_return = expected_return
        self.volatility = volatility
        self.years = years
        self.simulations = simulations

    def run(self):
        results = np.zeros((self.years + 1, self.simulations))
        results[0] = self.initial_investment

        for t in range(1, self.years + 1):
            random_returns = np.random.normal(
                self.expected_return,
                self.volatility,
                self.simulations,
            )
            results[t] = results[t - 1] * (1 + random_returns)

        return results

    def summary(self):
        results = self.run()
        final = results[-1]

        print("===== Monte Carlo Simulation =====")
        print(f"Average Value : ₹{final.mean():,.2f}")
        print(f"Median Value  : ₹{np.median(final):,.2f}")
        print(f"Minimum Value : ₹{final.min():,.2f}")
        print(f"Maximum Value : ₹{final.max():,.2f}")
