import joblib
import numpy as np
import pandas as pd  # Make sure pandas is imported
from .rules import apply_rules

# Load the trained model
model = joblib.load('models/logistic_model.pkl')

def hybrid_risk_score(debt_to_equity, cash_flow):
    """
    Calculates a hybrid risk score by combining a logistic regression model
    with a set of business rules.
    """
    # Create a DataFrame with feature names to prevent scikit-learn warnings
    input_df = pd.DataFrame([[debt_to_equity, cash_flow]],
                            columns=['debt_to_equity', 'cash_flow'])

    # Get prediction and confidence from the model
    model_pred = model.predict(input_df)[0]
    model_conf = model.predict_proba(input_df)[0][model_pred]
    model_label = "High Risk" if model_pred == 1 else "Low Risk"

    # Get assessment from the rule-based system
    rule_label = apply_rules(debt_to_equity, cash_flow)

    # Combine the model and rule logic
    if "High Risk" in rule_label and model_label == "Low Risk":
        final_label = "High Risk (Rule override)"
    elif "Low Risk" in rule_label and model_label == "High Risk":
        final_label = "Medium Risk (Model vs Rule conflict)"
    else:
        final_label = model_label

    # Convert numpy float to standard Python float for cleaner output
    confidence_float = float(round(model_conf, 2))

    return {
        "model": model_label,
        "confidence": confidence_float,
        "rule": rule_label,
        "final": final_label
    }