# Car Price Prediction using Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Step 1: Load Dataset
df = pd.read_csv("car data.csv")  # ✅ Your CSV file

# Step 2: Initial Exploration
print("🔹 First 5 rows of the dataset:\n", df.head())
print("\n🔹 Dataset Info:\n")
print(df.info())
print("\n🔹 Summary Statistics:\n", df.describe())

# Step 3: Check for Missing Values
print("\n🔹 Missing Values:\n", df.isnull().sum())

# Step 4: Label Encode Categorical Columns
le = LabelEncoder()
categorical_cols = ['Car_Name', 'Fuel_Type', 'Selling_type', 'Transmission']
print("\n🔹 Categorical Columns:", categorical_cols)

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Step 5: Define Features and Target
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

# Step 6: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Predict and Evaluate
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\n✅ Model Evaluation:")
print(f"R2 Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.2f}")

# Step 9: Visualization - Actual vs Predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='green', edgecolors='black')
plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Prices")
plt.grid(True)
plt.show()
