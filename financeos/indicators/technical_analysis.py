from financeos.indicators.technical_analysis import TechnicalAnalysis


def test_technical_analysis_creation():
    ta = TechnicalAnalysis()
    assert ta is not None
