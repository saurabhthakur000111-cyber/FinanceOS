import numpy as np


class MarkowitzOptimizer:
    def __init__(self, expected_returns, covariance_matrix):
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)

    def equal_weight_portfolio(self):
        n = len(self.expected_returns)
        return np.ones(n) / n

    def portfolio_return(self, weights):
        weights = np.array(weights)
        return float(np.dot(weights, self.expected_returns))

    def portfolio_risk(self, weights):
        weights = np.array(weights)
        variance = weights.T @ self.covariance_matrix @ weights
        return float(np.sqrt(variance))

    def sharpe_ratio(self, weights, risk_free_rate=0.02):
        port_return = self.portfolio_return(weights)
        port_risk = self.portfolio_risk(weights)

        if port_risk == 0:
            return 0.0

        return (port_return - risk_free_rate) / port_risk


if __name__ == "__main__":
    expected_returns = [0.12, 0.15, 0.10]

    covariance = [
        [0.10, 0.02, 0.04],
        [0.02, 0.08, 0.01],
        [0.04, 0.01, 0.07],
    ]

    optimizer = MarkowitzOptimizer(expected_returns, covariance)

    weights = optimizer.equal_weight_portfolio()

    print("Weights:", weights)
    print("Expected Return:", round(optimizer.portfolio_return(weights), 4))
    print("Risk:", round(optimizer.portfolio_risk(weights), 4))
    print("Sharpe Ratio:", round(optimizer.sharpe_ratio(weights), 4))
