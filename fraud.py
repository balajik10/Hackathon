from flask import Flask, request, jsonify
from xgboost import XGBClassifier
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = XGBClassifier()
model.load_model("path for model")  # Update with the actual path to your model file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Convert data to a DataFrame
        data_df = pd.DataFrame([data])

        # Make predictions
        prediction = model.predict(data_df)

        # Map prediction to 'Yes' or 'No'
        mapping = {1: 'Yes', 0: 'No'}
        predicted_fraud = mapping.get(prediction[0], 'Unknown')

        # Return the result as JSON
        result = {'prediction': predicted_fraud}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
