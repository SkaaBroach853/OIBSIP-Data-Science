import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (change filename if needed)
df = pd.read_csv("Unemployment.csv")

# Rename columns for clarity - adjust if your CSV has different columns/order
df.columns = ['State', 'Date', 'Frequency', 'Estimated Unemployment Rate',
              'Estimated Employed', 'Estimated Labour Participation Rate',
              'Region', 'Longitude', 'Latitude']

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with missing values if any
df = df.dropna()

# Basic data info
print("🔹 First 5 rows of the data:")
print(df.head(), "\n")

print("🔹 Dataset Info:")
print(df.info(), "\n")

print("🔹 Missing Values:")
print(df.isnull().sum(), "\n")

# Plot 1: Average Estimated Unemployment Rate by Region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Estimated Unemployment Rate', data=df, estimator=lambda x: sum(x)/len(x), ci=None)
plt.title('Average Estimated Unemployment Rate by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Average Unemployment Rate Over Time (All regions combined)
unemp_time = df.groupby('Date')['Estimated Unemployment Rate'].mean()

plt.figure(figsize=(12, 6))
plt.plot(unemp_time.index, unemp_time.values, marker='o')
plt.title('Average Estimated Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 3: Average Unemployment Rate by State
unemp_state = df.groupby('State')['Estimated Unemployment Rate'].mean().sort_values(ascending=False)

plt.figure(figsize=(14, 7))
sns.barplot(x=unemp_state.index, y=unemp_state.values, palette='viridis')
plt.title('Average Estimated Unemployment Rate by State')
plt.xlabel('State')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
