from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

model_path = "/Users/lavishvaishnav/Desktop/OLD_RJPOLICE_HACK_680_Sangyan_07/UPI_model.pkl"
model = joblib.load(model_path)


dataset_path = "/Users/lavishvaishnav/Desktop/OLD_RJPOLICE_HACK_680_Sangyan_07/upi_fraud_dataset.csv"
dataset = pd.read_csv(dataset_path)

scaler = StandardScaler()



@app.route('/predict', methods=['POST'])
def predict():

    try:
       
        data = request.get_json()


        data_df = pd.DataFrame([data])

       
        zero_fields = data_df.columns[data_df.iloc[0, :-1].eq(0)].tolist()

        if zero_fields:
            return jsonify({"error": f"Invalid input. The following fields have zero values: {', '.join(zero_fields)}"})

       
        user_upi_number = data['upi_number']
        user_data = dataset[dataset['upi_number'] == user_upi_number].drop(columns=['fraud_label'])
        
        # Scale the features using the previously created scaler
        data_scaled = scaler.transform(user_data)

        # Make the prediction
        prediction = model.predict(data_scaled)
        prediction_label = "Yes, it is fraud" if prediction[0] == 1 else "No, it is not fraud"

        result = {"prediction_label": prediction_label}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
