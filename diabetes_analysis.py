import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/diabetes.csv")

print("Dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

# Correlation with diabetes outcome
correlations = df.corr(numeric_only=True)["Outcome"].sort_values(ascending=False)

print("\nCorrelation with diabetes outcome:")
print(correlations)

# Save correlation results
correlations.to_csv("diabetes_correlations.csv")

# Plot 1: Correlation with diabetes outcome
plt.figure(figsize=(8, 5))
correlations.drop("Outcome").plot(kind="bar")
plt.title("Correlation of Risk Factors with Diabetes Outcome")
plt.ylabel("Correlation")
plt.xlabel("Risk Factor")
plt.tight_layout()
plt.savefig("diabetes_correlation_bar_chart.png")
plt.show()

# Plot 2: Average glucose by diabetes outcome
glucose_by_outcome = df.groupby("Outcome")["Glucose"].mean()

plt.figure(figsize=(6, 4))
glucose_by_outcome.plot(kind="bar")
plt.title("Average Glucose Level by Diabetes Outcome")
plt.ylabel("Average Glucose")
plt.xlabel("Diabetes Outcome")
plt.xticks([0, 1], ["No Diabetes", "Diabetes"], rotation=0)
plt.tight_layout()
plt.savefig("average_glucose_by_outcome.png")
plt.show()

# Plot 3: Average BMI by diabetes outcome
bmi_by_outcome = df.groupby("Outcome")["BMI"].mean()

plt.figure(figsize=(6, 4))
bmi_by_outcome.plot(kind="bar")
plt.title("Average BMI by Diabetes Outcome")
plt.ylabel("Average BMI")
plt.xlabel("Diabetes Outcome")
plt.xticks([0, 1], ["No Diabetes", "Diabetes"], rotation=0)
plt.tight_layout()
plt.savefig("average_bmi_by_outcome.png")
plt.show()

# Simple written insight
strongest_factor = correlations.drop("Outcome").idxmax()
strongest_corr = correlations.drop("Outcome").max()

print("\nKey Insight:")
print(f"The strongest correlation with diabetes outcome was {strongest_factor}, with a correlation of {strongest_corr:.2f}.")