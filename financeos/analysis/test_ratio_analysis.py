from financeos.analysis.ratio_analysis import RatioAnalysis


def test_current_ratio():
    ratio = RatioAnalysis(
        current_assets=500000,
        current_liabilities=250000,
        total_debt=400000,
        total_equity=600000,
        net_income=120000,
        total_assets=1000000,
        revenue=800000,
        gross_profit=320000,
        shares_outstanding=10000,
        market_price=333.02,
    )

    assert ratio.current_ratio() == 2


def test_debt_to_equity():
    ratio = RatioAnalysis(
        current_assets=500000,
        current_liabilities=250000,
        total_debt=400000,
        total_equity=600000,
        net_income=120000,
        total_assets=1000000,
        revenue=800000,
        gross_profit=320000,
        shares_outstanding=10000,
        market_price=333.02,
    )

    assert round(ratio.debt_to_equity(), 2) == 0.67
