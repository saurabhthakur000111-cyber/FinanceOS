from financeos.valuation.valuation import CompanyValuation


def test_company_valuation():
    company = CompanyValuation()

    assert company.current_price == 333.02
