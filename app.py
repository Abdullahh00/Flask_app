from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Initialize Flask application
app = Flask(__name__)

# Load the dataset
dataset_path = 'iris.csv'  # Make sure this path is correct
data = pd.read_csv(dataset_path)

# Prepare the data
X = data.drop('species', axis=1)
y = data['species']

# Split the dataset (you might want to use the whole dataset for training in production)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the logistic regression model
logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train, y_train)

# Define the predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the received JSON
        features = request.json
        features_df = pd.DataFrame(features, index=[0])
       
        # Make prediction
        prediction = logistic_model.predict(features_df)
       
        # Return prediction
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
