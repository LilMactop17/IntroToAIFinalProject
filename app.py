from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from sklearn.metrics import accuracy_score
import os

app = Flask(__name__, static_folder='static')

# ── Train the model on startup (same logic as main.py) ──────────────────────
df = pd.read_csv('Dataset.csv', encoding='latin-1')
df = df[['label', 'subject', 'body']]
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df = df.dropna(subset=['label', 'subject', 'body'])

X_train_sub, X_test_sub, X_train_body, X_test_body, y_train, y_test = train_test_split(
    df['subject'], df['body'], df['label'], test_size=0.2, random_state=42
)

vectorizer_sub  = CountVectorizer()
vectorizer_body = CountVectorizer(ngram_range=(1, 2))

X_train_sub_counts  = vectorizer_sub.fit_transform(X_train_sub)
X_train_body_counts = vectorizer_body.fit_transform(X_train_body)
X_train_combined    = hstack((X_train_sub_counts, X_train_body_counts))

model = MultinomialNB()
model.fit(X_train_combined, y_train)

# Quick accuracy check on hold-out set
X_test_sub_c  = vectorizer_sub.transform(X_test_sub)
X_test_body_c = vectorizer_body.transform(X_test_body)
y_pred        = model.predict(hstack((X_test_sub_c, X_test_body_c)))
MODEL_ACCURACY = round(accuracy_score(y_test, y_pred) * 100, 1)

print(f"Model ready — test-set accuracy: {MODEL_ACCURACY}%")

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data    = request.get_json(force=True)
    subject = data.get('subject', '')
    body    = data.get('body', '')

    sub_vec  = vectorizer_sub.transform([subject])
    body_vec = vectorizer_body.transform([body])
    combined = hstack((sub_vec, body_vec))

    prediction  = model.predict(combined)[0]
    proba       = model.predict_proba(combined)[0]
    confidence  = round(float(max(proba)) * 100, 1)

    return jsonify({
        'classification': 'spam' if prediction == 1 else 'ham',
        'confidence':     confidence,
        'model_accuracy': MODEL_ACCURACY,
    })

@app.route('/accuracy')
def accuracy():
    return jsonify({'accuracy': MODEL_ACCURACY})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
