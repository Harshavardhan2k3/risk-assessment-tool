# logic/rules.py

def apply_rules(debt_to_equity, cash_flow):
    # Rule 1: Very high debt-to-equity ratio
    if debt_to_equity > 3.0:
        return "High Risk (Rule: Excessive debt)"

    # Rule 2: Negative cash flow
    if cash_flow < 0:
        return "High Risk (Rule: Negative cash flow)"

    # Rule 3: Healthy financials
    if debt_to_equity < 2.0 and cash_flow > 10000:
        return "Low Risk (Rule: Strong financials)"

    # Default
    return "Medium Risk (Rule: borderline case)"