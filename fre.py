import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
print("First 5 Rows:")
print(df.head())
print("\nDataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="day", y="total_bill")
plt.title("Average Restaurant Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Restaurant Bills by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
plt.figure(figsize=(8, 5))
sns.stripplot(data=df, x="day", y="tip", jitter=True)
plt.title("Tips Given on Different Days")
plt.xlabel("Day")
plt.ylabel("Tip Amount")
plt.show()
plt.figure(figsize=(8, 5))
sns.stripplot(data=df, x="day", y="tip", jitter=True)
plt.title("Tips Given on Different Days")
plt.xlabel("Day")
plt.ylabel("Tip Amount")
plt.show()
plt.figure(figsize=(8, 5))
sns.swarmplot(data=df, x="day", y="total_bill")
plt.title("Distribution of Restaurant Bills")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()


# Part 9: Joint Plot
sns.jointplot(data=df, x="total_bill", y="tip", kind="scatter")
plt.show()


# Part 10: Pair Plot
sns.pairplot(df, hue="sex")
plt.show()


# Part 11: Point Plot
plt.figure(figsize=(8, 5))
sns.pointplot(data=df, x="day", y="tip", hue="sex")
plt.title("Average Tips by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()


# Part 12: Linear Regression Plot (lmplot)
sns.lmplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Relationship Between Total Bill and Tip")
plt.show()


# Part 13: Final Message
print("\nRestaurant Bill Explorer Completed Successfully!")
