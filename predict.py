import sys
import logging
import pickle

from flask import Flask, request
from flask_pydantic import validate

from src.employee_description import EmployeeData, EmployeeResponse

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_obj(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

encoder = load_obj('models/encoder.pkl')
scaler = load_obj('models/scaler.pkl')
model = load_obj('models/model.pkl')

app = Flask('attrition_prediction')


@app.get('/')
def main():
    return 'Welcome to the Employee Attrition prediction webservice!'


@app.route('/predict', methods=['POST'])
@validate()
def predict():
    employee_features = request.get_json()

    X = encoder.transform(employee_features)

    X_scaled = scaler.transform(X)
    y_pred = model.predict_proba(X_scaled)[0, 1]
    attrition = y_pred >= 0.25
    return EmployeeResponse(probability=float(y_pred), attrition=attrition)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
