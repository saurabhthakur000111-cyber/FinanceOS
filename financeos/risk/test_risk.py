from financeos.risk.risk_engine import RiskEngine


def test_risk_engine_creation():
    risk = RiskEngine()
    assert risk is not None
