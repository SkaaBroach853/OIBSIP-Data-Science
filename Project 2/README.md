# 📊 Unemployment Analysis in India (2020) — AICTE OASIS InfoByte Internship Task 2

This project is part of the **AICTE OASIS InfoByte Data Science Internship**, specifically **Task 2: Unemployment Analysis**.

We analyze unemployment data for various Indian states during the year 2020 using **Python**. This includes data visualization, trend analysis, and comparison across regions and states.

---

## 📁 Files in This Repository

| File | Description |
|------|-------------|
| `unemployment_analysis.py` | Python script that performs all data analysis and visualization |
| `Unemployment_Rate_upto_11_2020.csv` | Dataset containing unemployment data |
| `requirements.txt` | Required libraries for the project |
| `video_script.txt` | Script you can use to record your explanation video |
| `README.md` | This detailed file describing the project |

---

## 📊 About the Dataset

The dataset contains monthly unemployment data for various states in India during **January–November 2020**, a period heavily impacted by COVID-19.

**Key columns:**
- `State`: Name of the Indian state
- `Date`: Time of data collection (monthly)
- `Estimated Unemployment Rate`: % of unemployed individuals
- `Estimated Employed`: Count of employed individuals
- `Estimated Labour Participation Rate`: Total labor force involvement
- `Region`: Geographical region (North, South, etc.)
- `Longitude`, `Latitude`: Geolocation for mapping

---

## 🔍 What This Project Does

1. **Loads the dataset**
2. **Cleans the data**: Renames columns, handles missing values, converts date column
3. **Explores the data**: Displays first few rows, dataset info, null values
4. **Visualizes**:
   - Average unemployment rate by region
   - Unemployment rate trend over time
   - Average unemployment rate by state

---

## 📈 Visualizations Created

- **Bar Chart**: Average Unemployment Rate by Region  
- **Line Chart**: Unemployment Rate Over Time  
- **Bar Chart**: Unemployment Rate by State  

All charts are generated using **Matplotlib** and **Seaborn**.

---

## 🧑‍💻 Technologies Used

- **Python** (v3.8+)
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Unemployment-Analysis.git
cd Unemployment-Analysis
```
---
## 2. Install dependencies
Create a virtual environment (optional but recommended):

```bash

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```
Then install the required libraries:

```bash

pip install -r requirements.txt
```

## 3. Run the analysis script
```bash

python unemployment_analysis.py
```
---
## ✍️ Author
- Name: Aaditya Devadiga
- Internship: AICTE OASIS InfoByte — Data Science
