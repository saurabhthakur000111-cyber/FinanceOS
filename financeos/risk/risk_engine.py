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

        # Volatility Risk
        if volatility > 0.30:
            score -= 30
        elif volatility > 0.15:
            score -= 15

        # Debt Risk
        if debt_ratio > 0.70:
            score -= 30
        elif debt_ratio > 0.40:
            score -= 15

        # Liquidity Risk
        if liquidity_ratio < 1:
            score -= 20

        return max(score, 0)

    def calculate_risk(self):

        # Sample values
        volatility = 0.18
        debt_ratio = 0.35
        liquidity_ratio = 2.0

        risk = self.calculate_risk_score(
            volatility,
            debt_ratio,
            liquidity_ratio
        )

        print("========== RISK REPORT ==========")
        print(f"Volatility      : {volatility:.2f}")
        print(f"Debt Ratio      : {debt_ratio:.2f}")
        print(f"Liquidity Ratio : {liquidity_ratio:.2f}")
        print(f"Risk Score      : {risk}")

        if risk >= 80:
            print("Risk Level      : LOW")
        elif risk >= 60:
            print("Risk Level      : MEDIUM")
        else:
            print("Risk Level      : HIGH")


if __name__ == "__main__":

    engine = RiskEngine()
    engine.calculate_risk()