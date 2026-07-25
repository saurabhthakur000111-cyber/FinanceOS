class RiskEngine:

    def __init__(self):
        pass

    def calculate_risk_score(
        self,
        volatility,
        debt_ratio,
        liquidity_ratio
    ):

        score = 100

        # volatility risk
        if volatility > 0.30:
            score -= 30
        elif volatility > 0.15:
            score -= 15

        # debt risk
        if debt_ratio > 0.70:
            score -= 30
        elif debt_ratio > 0.40:
            score -= 15

        # liquidity protection
        if liquidity_ratio < 1:
            score -= 20

        return max(score, 0)


if __name__ == "__main__":

    engine = RiskEngine()

    risk = engine.calculate_risk_score(
        volatility=0.18,
        debt_ratio=0.35,
        liquidity_ratio=2
    )

    print("========== RISK REPORT ==========")
    print("Risk Score :", risk)