# spam_detector.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Step 1: Load the dataset
try:
    data = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
    data.columns = ['label', 'message']
except FileNotFoundError:
    print("❗ Error: 'spam.csv' not found. Make sure it is in the same folder as this script.")
    exit()

# 🔹 Step 2: Preprocessing - Convert labels to numbers (ham = 0, spam = 1)
data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

# 🔹 Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.2, random_state=42)

# 🔹 Step 4: Text Vectorization using Bag of Words
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 🔹 Step 5: Model Training using Naive Bayes
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 🔹 Step 6: Predict on Test Data
y_pred = model.predict(X_test_vec)

# 🔹 Step 7: Evaluation Metrics
print("\n🔍 Accuracy:", accuracy_score(y_test, y_pred))

print("\n📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\n📈 Classification Report:\n", classification_report(y_test, y_pred))

# 🔹 Step 8: Visualization of Confusion Matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("📊 Confusion Matrix - Spam Detection")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
