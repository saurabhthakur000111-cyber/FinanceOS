from financeos.ai.financial_ai import FinancialAI


def test_ai_creation():
    ai = FinancialAI()
    assert ai is not None
