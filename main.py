import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Loading our dataset
df = pd.read_csv('Dataset.csv', encoding='latin-1')
df = df[['label', 'subject', 'body']].rename(columns={'v1': 'label', 'v2': 'subject', 'v3': 'body'})

# Mapping ham/spam labels to numbers for the naive bayes algorithm
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Splitting data, 20% to test on.
X_train_sub,  X_test_sub, X_train_body, X_test_body, y_train, y_test = train_test_split(df['subject'], df['body'], df['label'], test_size=0.2)

# Vectorize our dataset to bag-of-words representation for naive bayes
vectorizer_sub = CountVectorizer()
vectorizer_body = CountVectorizer(ngram_range=(1, 2))

X_train_sub_counts = vectorizer_sub.fit_transform(X_train_sub)
X_train_body_counts = vectorizer_body.fit_transform(X_train_body)

# Subject and body are judged separately, as subject can be a dead giveaway and have different context.
X_train_combined = hstack((X_train_sub_counts, X_train_body_counts))

# Training the model on the combined dataset
model = MultinomialNB()
model.fit(X_train_combined, y_train)

# Vectorize test subset for accuracy purposes
X_test_sub = vectorizer_sub.transform(X_test_sub)
X_test_body = vectorizer_body.transform(X_test_body)
X_test_combined = hstack((X_test_sub, X_test_body))

y_pred = model.predict(X_test_combined)

# Print accuracy metrics
print("Accuracy: ", f"{accuracy_score(y_test, y_pred):.2f}")
print("Confusion matrix: ")
print(confusion_matrix(y_test, y_pred))
print("Classification report: ")
print(classification_report(y_test, y_pred))

# Testing Loop
while(True):
    new_msg_sub = input("Enter email subject: ")
    new_msg_body = input("Enter email body: ")
    new_msg_sub_counts = vectorizer_sub.transform([new_msg_sub])
    new_msg_body_counts = vectorizer_body.transform([new_msg_body])
    new_msg_combined = hstack((new_msg_sub_counts, new_msg_body_counts))
    prediction = model.predict(new_msg_combined)
    print("Spam" if prediction[0] == 1 else "Ham")
