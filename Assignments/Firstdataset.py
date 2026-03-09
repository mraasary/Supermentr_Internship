import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 60, 65, 72, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Feature and Label
X = df[["Study_Hours"]]   # Feature
y = df["Marks"]           # Label

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict marks
predicted_marks = model.predict(X)

# Plot dataset with regression line
sns.set_style("whitegrid")

plt.figure(figsize=(8,5))
plt.scatter(df["Study_Hours"], df["Marks"], label="Actual Data")
plt.plot(df["Study_Hours"], predicted_marks, label="Regression Line")
plt.title("Study Hours vs Marks Prediction")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()

