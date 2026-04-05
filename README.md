# SPAM.FILTER — Frontend for your Naive Bayes classifier

## How to run

1. Install dependencies:
   ```
   pip install flask pandas scikit-learn scipy
   ```

2. Start the server (trains the model automatically):
   ```
   python app.py
   ```

3. Open your browser to:
   ```
   http://localhost:5000
   ```

That's it! The UI lets you enter an email subject + body and classifies it as **ham** or **spam** using your exact trained model.

## Files
- `app.py`        — Flask server wrapping your Naive Bayes model
- `main.py`       — Original classifier (unchanged)
- `Dataset.csv`   — Training data
- `static/index.html` — Frontend UI (served by Flask)
