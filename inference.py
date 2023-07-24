import pickle
import pandas as pd
import numpy as np
from flask import Flask, request

# PART C
# 2. Load the trained model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 3. Load the test data and expected predictions
X_test = pd.read_csv('X_test.csv')
preds = np.loadtxt('preds.csv', delimiter=',')
print((model.predict(X_test) == preds).all())

app = Flask(__name__)

@app.route('/predict_churn', methods=['GET'])
def predict_churn():
    """
    Predict the churn based on input parameters.
    """
    # Get the input parameters from the query parameters
    is_male = float(request.args.get('key1'))
    num_inters = float(request.args.get('key2'))
    late_on_payment = float(request.args.get('key3'))
    age = float(request.args.get('key4'))
    years_in_contract = float(request.args.get('key5'))

    # Perform the prediction using the loaded model
    prediction = model.predict([[is_male, num_inters, late_on_payment, age, years_in_contract]])[0]

    # Return the prediction as a string
    return str(prediction)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)