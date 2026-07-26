from ai_assistant.financial_prompts import SYSTEM_PROMPT


def generate_analysis(
    company,
    financial_data=None
):

    response = f"""

FinanceOS AI Analysis

Company:
{company}


Fundamental View:
Analyze revenue growth,
profitability,
debt levels,
and business quality.


Risk View:
Evaluate volatility,
sector exposure,
and downside risks.


Valuation View:
Compare intrinsic value,
market price,
and margin of safety.


Portfolio Impact:
Explain how this security
affects diversification.

"""


    return response
