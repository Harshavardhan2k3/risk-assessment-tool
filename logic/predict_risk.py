{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f023f11d-1530-4201-84d6-291b1b871158",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('models/logistic_model.pkl')\n",
    "\n",
    "def predict_risk(debt_to_equity, cash_flow):\n",
    "    # Prepare input data\n",
    "    input_data = np.array([[debt_to_equity, cash_flow]])\n",
    "    \n",
    "    # Predict risk\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    probability = model.predict_proba(input_data)[0][prediction]\n",
    "    \n",
    "    # Interpret result\n",
    "    risk_label = \"High Risk\" if prediction == 1 else \"Low Risk\"\n",
    "    print(f\"Prediction: {risk_label} (Confidence: {probability:.2f})\")\n",
    "    return risk_label, probability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53348b2b-729a-47dc-ae88-13113f2e6b02",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
