from financeos.optimization import MarkowitzOptimizer


def test_markowitz_optimizer():
    expected_returns = [0.12, 0.15, 0.10]

    covariance = [
        [0.10, 0.02, 0.04],
        [0.02, 0.08, 0.01],
        [0.04, 0.01, 0.07],
    ]

    optimizer = MarkowitzOptimizer(expected_returns, covariance)

    weights = optimizer.equal_weight_portfolio()

    assert len(weights) == 3
    assert abs(sum(weights) - 1.0) < 1e-9
    assert optimizer.portfolio_return(weights) > 0
    assert optimizer.portfolio_risk(weights) > 0
    assert optimizer.sharpe_ratio(weights) > 0
