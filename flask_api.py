from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the saved model, scaler, feature names and feature means
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')
feature_means = joblib.load('feature_means.pkl')

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data sent in the request
    data = request.get_json()
    
    # Start with average values for all 83 features
    input_data = pd.DataFrame([feature_means], columns=feature_names)
    
    # Override with values provided by the user
    for key, value in data.items():
        if key in feature_names:
            input_data[key] = value
    
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction and reverse log transformation
    prediction = model.predict(input_scaled)
    predicted_price = np.expm1(prediction[0])
    
    # Return the prediction as JSON
    return jsonify({
        'predicted_price': round(float(predicted_price), 2),
        'currency': 'USD'
    })

# Define a home route to confirm the API is running
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'House Price Prediction API is running',
        'endpoint': '/predict',
        'method': 'POST'
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    