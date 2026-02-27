import pandas as pd

# Load dataset
url = "https://calmcode.io/static/data/titanic.csv"
df = pd.read_csv(url)

# 1. Display top rows
print("Top 5 Rows:\n")
print(df.head())

# 2. Find highest value column
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
max_values = numeric_cols.max()

print("\nColumn with Highest Value:\n")
print(max_values.idxmax(), "=", max_values.max())

# 3. Count missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# 4. Five Insights
print("\nFive Insights:\n")

print("1. Overall Survival Rate:")
print(round(df['survived'].mean() * 100, 2), "%")
print("-" * 40)

print("2. Survival Rate by Gender:")
print(df.groupby('sex')['survived'].mean() * 100)
print("-" * 40)

print("3. Survival Rate by Passenger Class:")
print(df.groupby('pclass')['survived'].mean() * 100)
print("-" * 40)

print("4. Average Fare:")
print(round(df['fare'].mean(), 2))
print("-" * 40)

print("5. Missing Age Values:")
print(df['age'].isnull().sum())
print("-" * 40)