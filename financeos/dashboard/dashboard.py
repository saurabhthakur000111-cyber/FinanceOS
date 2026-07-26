from financeos.market.market_data import MarketData
from financeos.ai.financial_ai import FinancialAI
from financeos.analysis.ratio_analysis import RatioAnalysis
from financeos.portfolio.portfolio import Portfolio
from financeos.risk.risk_engine import RiskEngine
from financeos.fundamentals.financial_statements import FinancialStatements


def main():

    print("\n==============================")
    print("      FINANCEOS DASHBOARD")
    print("==============================\n")

    # ====================================
    # 1. Live Market Data
    # ====================================

    print("1. Live Market Data")

    market = MarketData()
    stock = market.get_stock("AAPL")

    print("========== LIVE STOCK DATA ==========")

    for key, value in stock.items():
        print(f"{key} : {value}")

    print("\n------------------------------")

    # ====================================
    # 2. AI Recommendation
    # ====================================

    print("2. AI Recommendation")

    ai = FinancialAI()
    ai.analyze("AAPL")

    print("\n------------------------------")

    # ====================================
    # 3. Financial Ratios
    # ====================================

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

    # ====================================
    # 4. Portfolio
    # ====================================

    print("4. Portfolio")

    portfolio = Portfolio()
    portfolio.show_portfolio()

    print("\n------------------------------")

    # ====================================
    # 5. Risk Assessment
    # ====================================

    print("5. Risk Assessment")

    risk = RiskEngine()
    risk.calculate_risk()

    print("\n------------------------------")

    # ====================================
    # 6. Financial Statements
    # ====================================

    print("6. Financial Statements")

    statements = FinancialStatements("AAPL")
    statements.show_all()

    print("\n==============================")
    print(" Dashboard Completed Successfully ")
    print("==============================")


if __name__ == "__main__":
    main()