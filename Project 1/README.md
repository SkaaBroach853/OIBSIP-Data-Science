# 🌸 Iris Flower Classification using Machine Learning
**AICTE OASIS Infobyte Data Science Internship – Task 1**

---

## 📌 Project Overview

This project aims to classify Iris flowers into three different species — **Setosa**, **Versicolor**, and **Virginica** — using a **supervised machine learning algorithm**. The classification is based on four important features:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

We use **Logistic Regression**, a simple yet effective algorithm for multi-class classification, to build the model.

---

## 📂 Dataset Description

We use the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/Iris), which is a multivariate dataset introduced by the British biologist and statistician Ronald Fisher in 1936.

**Dataset File**: `Iris.csv`  
**Total Samples**: 150  
**Columns:**

| Column Name      | Description                          |
|------------------|--------------------------------------|
| `Id`             | Serial number (not needed)           |
| `SepalLengthCm`  | Length of the sepal (in cm)          |
| `SepalWidthCm`   | Width of the sepal (in cm)           |
| `PetalLengthCm`  | Length of the petal (in cm)          |
| `PetalWidthCm`   | Width of the petal (in cm)           |
| `Species`        | Type of iris flower (target label)   |

---

## 🛠️ Technologies & Libraries Used

| Tool/Library      | Purpose                          |
|-------------------|----------------------------------|
| Python            | Programming Language             |
| Pandas            | Data manipulation and analysis   |
| Matplotlib        | Plotting and data visualization  |
| Seaborn           | Advanced visualization            |
| Scikit-learn      | Machine Learning toolkit         |

---

## 🔄 Workflow of the Project

### 1. **Import Libraries**

We import necessary libraries like `pandas`, `matplotlib`, `seaborn`, and `sklearn`.

### 2. **Load and Explore Dataset**

- Load `Iris.csv` using pandas.
- Drop the `Id` column since it’s not useful for prediction.
- Display the first 5 rows and dataset info.

### 3. **Data Visualization**

- Use `seaborn.pairplot()` to visualize pairwise relationships between features, colored by species.

### 4. **Data Preparation**

- Separate the features (`X`) and label (`y`)
- Split the dataset into training and testing sets (80:20 split)

### 5. **Model Building**

- Train a **Logistic Regression** model on the training data

### 6. **Model Evaluation**

- Predict the labels for the test data
- Evaluate using:
  - Accuracy Score
  - Classification Report (precision, recall, f1-score)

---

## 📊 Output

### ✅ Sample Console Output:
<img width="858" alt="Screenshot 2025-06-08 134847" src="https://github.com/user-attachments/assets/fa40a908-4977-4d09-9deb-30c3345be2b3" />


---
## 🙌 Author
- Name - Aaditya Devadiga
- AICTE OASIS Infobyte Internship - Data Science
- Task 1 – Iris Flower Classification
## 📌 License
**This project is open-source and available under the MIT License.**
