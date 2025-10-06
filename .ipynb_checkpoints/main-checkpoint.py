# main.py

from logic.hybrid_score import hybrid_risk_score

def run_assessment():
    """
    Main function to run the client risk assessment tool.
    It prompts the user for inputs, validates them, and prints the assessment.
    """
    print("-" * 50)
    print("      Client-Side Risk Assessment Tool")
    print("-" * 50)

    try:
        # Get user input for financial metrics
        debt_to_equity = float(input("Enter the client's Debt-to-Equity Ratio (e.g., 2.5): "))
        cash_flow = float(input("Enter the client's Cash Flow (e.g., -10000): "))

        # Get the hybrid risk score from our logic module
        assessment = hybrid_risk_score(debt_to_equity, cash_flow)

        # Print the results in a clean, user-friendly format
        print("\n--- Assessment Complete ---")
        print(f"  Final Risk Profile: {assessment['final']}")
        print("---------------------------")
        print(f"  Details:")
        print(f"    - Model Prediction: {assessment['model']} (Confidence: {assessment['confidence']})")
        print(f"    - Rule-Based Check: {assessment['rule']}")
        print("-" * 27)

    except ValueError:
        print("\n[Error] Invalid input. Please enter numerical values only.")
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_assessment()