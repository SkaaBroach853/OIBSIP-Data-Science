# 📧 Email Spam Detection using Machine Learning

This project detects spam emails using the Naive Bayes classifier and text processing techniques.

## 📂 Dataset
The dataset contains labeled emails as `spam` or `ham`.

## 📌 Technologies Used
- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Naive Bayes
- Matplotlib & Seaborn

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the script:
python spam_detector.py


## ✅ Output
- Accuracy score
- Confusion matrix
- Classification report
---
## ✅ Expected Outputs
- Accuracy (e.g., ~97%)
- Confusion Matrix Heatmap
- Classification Report (Precision, Recall, F1-Score)
---

## 🚀 How It Works
- Loads CSV dataset and selects relevant columns.

-Converts labels (ham, spam) to binary (0, 1).

- Splits dataset into training and testing sets.

- Transforms text data into numeric form using CountVectorizer.

- Trains a Naive Bayes classifier on the training data.

- Predicts and evaluates using:

  - Accuracy

  - Confusion Matrix

  - Classification Report

  - Visualizes the results with a heatmap.
---
## 🙋‍♂️ Author
- Name: Aaditya Devadiga
- Internship: AICTE OASIS INFOBYTE Data Science SIP
