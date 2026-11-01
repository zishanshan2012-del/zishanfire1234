
# World Animals Explorer

# Part 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Part 2: Load Penguins Dataset
df = sns.load_dataset("penguins")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Part 3: Inspect the Dataset
print("\nDataset Information:")
print(df.info())

print("\nDataset Description:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Part 4: Clean the Data
df = df.dropna()

print("\nCleaned Dataset:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Part 5: Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="body_mass_g", bins=20, kde=True)
plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Number of Penguins")
plt.show()

# Part 6: KDE Plot
plt.figure(figsize=(8, 5))
sns.kdeplot(
    data=df,
    x="flipper_length_mm",
    hue="species",
    fill=True
)
plt.title("Flipper Length Distribution by Species")
plt.xlabel("Flipper Length (mm)")
plt.show()

# Part 7: Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    style="sex",
    s=80
)
plt.title("Penguin Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()

# Part 8: Heatmap
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap of Penguin Measurements")
plt.show()

# Part 9: Pair Plot
sns.pairplot(
    df,
    hue="species",
    diag_kind="hist"
)
plt.show()

# Part 10: Count Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="species", hue="species")
plt.title("Number of Penguins by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Count")
plt.show()

print("\nWorld Animals Explorer Completed Successfully!")


