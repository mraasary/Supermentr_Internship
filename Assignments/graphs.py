import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

# -------------------------
# 1. BAR CHART
# -------------------------

courses = ['Computer Science', 'Mechanical', 'Civil', 'Electronics']
students = [120, 80, 60, 70]

df_bar = pd.DataFrame({
    'Course': courses,
    'Students': students
})

plt.figure(figsize=(8,5))
sns.barplot(x='Course', y='Students', data=df_bar)
plt.title("Number of Students in Different Courses")
plt.xlabel("Course")
plt.ylabel("Number of Students")

plt.savefig("bar_chart.png")
plt.show()

# -------------------------
# 2. PIE CHART
# -------------------------

labels = ['Computer Science', 'Mechanical', 'Civil', 'Electronics']
sizes = [40, 25, 15, 20]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Student Distribution by Department")

plt.savefig("pie_chart.png")
plt.show()

# -------------------------
# 3. HISTOGRAM
# -------------------------

scores = [45, 50, 55, 60, 62, 65, 68, 70, 72, 74, 75, 77, 78, 80, 82, 85, 87, 90, 92, 95]

plt.figure(figsize=(8,5))
sns.histplot(scores, bins=6, kde=True)
plt.title("Distribution of Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.savefig("histogram.png")
plt.show()