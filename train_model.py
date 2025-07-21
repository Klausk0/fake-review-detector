import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

# Load dataset
df = pd.read_csv("data/reviews.csv")

# Clean nulls
df.dropna(subset=["text_", "label"], inplace=True)


# Simple train/test split
X_train, X_test, y_train, y_test = train_test_split(df["text_"], df["label"], test_size=0.2, random_state=42)

# Define pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=3000, stop_words="english")),
    ("clf", LogisticRegression(solver="liblinear"))
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# Save vectorizer and classifier separately
vectorizer = pipeline.named_steps["tfidf"]
classifier = pipeline.named_steps["clf"]

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Save
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(classifier, "models/classifier.pkl")

print("✅ Models saved to models/")
