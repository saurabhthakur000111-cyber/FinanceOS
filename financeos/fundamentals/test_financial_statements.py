from financeos.fundamentals.financial_statements import FinancialStatements


def test_financial_statements_creation():
    fs = FinancialStatements("AAPL")

    assert fs.symbol == "AAPL"
