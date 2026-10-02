import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load cleaned data
df = pd.read_csv('../data/cleaned_data.csv')

print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe(include='all'))

# ===== INSIGHT 1: Salary distribution by Department_Region =====
plt.figure(figsize=(10, 6))
dept_salary = df.groupby('Department_Region')['Salary'].mean().sort_values(ascending=False)
dept_salary.plot(kind='bar', color='steelblue')
plt.title('Average Salary by Department/Region')
plt.xlabel('Department/Region')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../data/chart1_salary_by_department.png')
plt.close()
print("\nInsight 1: Average Salary by Department/Region:\n", dept_salary)

# ===== INSIGHT 2: Age distribution =====
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, color='coral', edgecolor='black')
plt.title('Employee Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('../data/chart2_age_distribution.png')
plt.close()
print("\nInsight 2: Age stats -> Mean:", df['Age'].mean(), "Median:", df['Age'].median())

# ===== INSIGHT 3: Performance Score vs Remote Work =====
plt.figure(figsize=(8, 6))
sns.countplot(x='Remote_Work', hue='Performance_Score', data=df)
plt.title('Performance Score Distribution: Remote vs Non-Remote')
plt.xlabel('Remote Work')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('../data/chart3_performance_remote.png')
plt.close()
print("\nInsight 3: Performance Score by Remote Work:\n", df.groupby(['Remote_Work', 'Performance_Score']).size())

# ===== INSIGHT 4: Employee count by Department_Region =====
plt.figure(figsize=(10, 6))
region_counts = df['Department_Region'].value_counts()
region_counts.plot(kind='bar', color='mediumseagreen')
plt.title('Employee Count by Department/Region')
plt.xlabel('Department/Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../data/chart4_region_distribution.png')
plt.close()
print("\nInsight 4: Employee Count by Department/Region:\n", region_counts)

# ===== INSIGHT 5: Status breakdown =====
plt.figure(figsize=(8, 8))
status_counts = df['Status'].value_counts()
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Employee Status Breakdown')
plt.tight_layout()
plt.savefig('../data/chart5_status_breakdown.png')
plt.close()
print("\nInsight 5: Status Breakdown:\n", status_counts)

# ===== BONUS: Correlation heatmap =====
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('../data/chart6_correlation_heatmap.png')
plt.close()

# ===== Anomaly detection: Salary outliers =====
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Salary'] < Q1 - 1.5*IQR) | (df['Salary'] > Q3 + 1.5*IQR)]
print("\nBonus Insight: Salary outliers found:", len(outliers))
print(outliers[['Employee_ID', 'Salary']])

print("\n===== ALL CHARTS SAVED TO data/ FOLDER =====")