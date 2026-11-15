import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("penguins")
print("First 5 Rows:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nDataset Description:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
df = df.dropna()

print("\nCleaned Dataset:")
print(df.head())
print("\nPenguin Species Count:")
print(df["species"].value_counts())
print("\nAverage Measurements by Species:")
print(df.groupby("species"))
["bill_length_mm", "bill_depth_mm",
     "flipper_length_mm", "body_mass_g"]
plt.show()
plt.ylabel("Body Mass (g)")
plt.show()
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="species", hue="species")
plt.title("Number of Penguins by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)
plt.title("Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="species", y="bill_length_mm")
plt.title("Bill Length by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Bill Length (mm)")
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="body_mass_g",
    hue="species",
    kde=True
)
plt.title("Penguin Body Mass Distribution")
plt.xlabel("Body Mass (g)")
plt.show()
sns.pairplot(
    df,
    hue="species",
    vars=[
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g"
    ]
)
plt.show()
plt.figure(figsize=(8, 5))
numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Penguin Characteristics Correlation")
plt.show()
print("\nCapstone Project Completed!")
print("Penguin Species Explorer")
print("Species:", df["species"].unique())
print("Total Penguins:", len(df))