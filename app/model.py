import joblib
import os
from cleaner import clean_text

# Load once
vectorizer = joblib.load("models/vectorizer.pkl")
classifier = joblib.load("models/classifier.pkl")

def predict_review_label(review_text):
    cleaned = clean_text(review_text)
    vector = vectorizer.transform([cleaned])
    prediction = classifier.predict(vector)[0]
    prob = classifier.predict_proba(vector)[0].max()
    return "Fake" if prediction == 1 else "Genuine", round(prob * 100, 2)
