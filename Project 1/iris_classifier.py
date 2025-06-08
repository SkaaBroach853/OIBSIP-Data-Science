# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset from CSV
df = pd.read_csv("Iris.csv")

# View the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Drop the ID column if it exists
if 'Id' in df.columns:
    df.drop(columns='Id', inplace=True)

# Rename columns (optional for clarity)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Visualize the data
sns.pairplot(df, hue="species")
plt.title("Iris Feature Pairplot")
plt.show()

# Prepare data
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)
print(f"\nPredicted species for sample {sample[0]}: {prediction[0]}")

