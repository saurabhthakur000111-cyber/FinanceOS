from financeos.market.market_data import MarketData
from financeos.ai.financial_ai import FinancialAI
from financeos.analysis.ratio_analysis import RatioAnalysis
from financeos.portfolio.portfolio import Portfolio
from financeos.risk.risk_engine import RiskEngine
from financeos.fundamentals.financial_statements import FinancialStatements
from financeos.valuation.valuation import CompanyValuation


def main():

    print("\n==============================")
    print("      FINANCEOS DASHBOARD")
    print("==============================\n")

    # ==========================
    # 1. Live Market Data
    # ==========================

    print("1. Live Market Data")

    market = MarketData()
    stock = market.get_stock("AAPL")

    print("========== LIVE STOCK DATA ==========")

    for key, value in stock.items():
        print(f"{key} : {value}")

    print("\n------------------------------")

    # ==========================
    # 2. AI Recommendation
    # ==========================

    print("2. AI Recommendation")

    ai = FinancialAI()
    ai.analyze("AAPL")

    print("\n------------------------------")

    # ==========================
    # 3. Financial Ratios
    # ==========================

    print("3. Financial Ratios")

    ratios = RatioAnalysis(
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
    print(f"Current Ratio : {ratios.current_ratio():.2f}")
    print(f"Debt/Equity   : {ratios.debt_to_equity():.2f}")
    print(f"ROE           : {ratios.roe():.2%}")
    print(f"ROA           : {ratios.roa():.2%}")
    print(f"Gross Margin  : {ratios.gross_margin():.2%}")
    print(f"Net Margin    : {ratios.net_margin():.2%}")
    print(f"EPS           : ₹{ratios.eps():.2f}")
    print(f"P/E Ratio     : {ratios.pe_ratio():.2f}")

    print("\n------------------------------")

    # ==========================
    # 4. Portfolio
    # ==========================

    print("4. Portfolio")

    portfolio = Portfolio()

    portfolio.add_asset("AAPL", 10, 333.02)
    portfolio.add_asset("MSFT", 5, 381.70)
    portfolio.add_asset("GOOG", 3, 319.09)

    portfolio.show()

    print("\n------------------------------")

    # ==========================
    # 5. Risk Assessment
    # ==========================

    print("5. Risk Assessment")

    risk = RiskEngine()

    score = risk.calculate_risk_score(
        volatility=0.18,
        debt_ratio=0.35,
        liquidity_ratio=2
    )

    print("========== RISK REPORT ==========")
    print("Volatility      : 0.18")
    print("Debt Ratio      : 0.35")
    print("Liquidity Ratio : 2.00")
    print(f"Risk Score      : {score}")

    if score >= 80:
        print("Risk Level      : LOW")
    elif score >= 60:
        print("Risk Level      : MEDIUM")
    else:
        print("Risk Level      : HIGH")

    print("\n------------------------------")

    # ==========================
    # 6. Financial Statements
    # ==========================

    print("6. Financial Statements")

    statements = FinancialStatements("AAPL")
    statements.show_all()

    print("\n------------------------------")

    # ==========================
    # 7. Company Valuation
    # ==========================

    print("7. Company Valuation")

    valuation = CompanyValuation()
    valuation.show()

    print("\n==============================")
    print(" Dashboard Completed Successfully ")
    print("==============================")


if __name__ == "__main__":
    main()