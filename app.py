from flask import Flask, request, jsonify, render_template
import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

app = Flask(__name__)


def preprocess_text(text):
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.strip()  # Remove leading/trailing whitespace
    return text


# Function to train the Logistic Regression model using a pipeline
def train_model():
    df = pd.read_csv('chat_dataset.csv')
    df['message'] = df['message'].apply(preprocess_text)

    X = df['message']
    y = df['sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    p = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', LogisticRegression())
    ])

    p.fit(X_train, y_train)

    joblib.dump(p, 'sentiment_model.joblib')

    return p


try:
    p = joblib.load('sentiment_model.joblib')
except:
    p = train_model()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        review = request.json['review']
        processed_review = preprocess_text(review)
        prediction = p.predict([processed_review])[0]

        sentiment = 'Positive' if prediction == 'positive' else 'Negative' if prediction == 'negative' else 'Neutral'

        return jsonify({'sentiment': sentiment})

    except Exception as e:

        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
