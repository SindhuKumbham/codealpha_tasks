import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# STEP 1 - Load Dataset
# =====================================================

df = pd.read_csv("books_dataset.csv")

# =====================================================
# STEP 2 - Show First 5 Rows
# =====================================================

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

# =====================================================
# STEP 3 - Dataset Information
# =====================================================

print("\n========== DATASET INFO ==========\n")
print(df.info())

# =====================================================
# STEP 4 - Shape of Dataset
# =====================================================

print("\n========== SHAPE OF DATASET ==========\n")
print(df.shape)

# =====================================================
# STEP 5 - Missing Values
# =====================================================

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# =====================================================
# STEP 6 - Duplicate Rows
# =====================================================

print("\n========== DUPLICATE ROWS ==========\n")
print(df.duplicated().sum())

# =====================================================
# STEP 7 - Statistical Summary
# =====================================================

print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())

# =====================================================
# STEP 8 - Rating Distribution Graph
# =====================================================

plt.figure(figsize=(8,5))

sns.countplot(x='Rating (1-5)', data=df)

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")

plt.show()

# =====================================================
# STEP 9 - Price Category Distribution
# =====================================================

plt.figure(figsize=(8,5))

sns.countplot(x='Price Category', data=df)

plt.title("Price Category Distribution")
plt.xlabel("Price Category")
plt.ylabel("Number of Books")

plt.xticks(rotation=45)

plt.show()

# =====================================================
# STEP 10 - Histogram of Prices
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(df['Price (GBP)'], bins=10)

plt.title("Price Distribution")
plt.xlabel("Price in GBP")
plt.ylabel("Count")

plt.show()

# =====================================================
# STEP 11 - Boxplot for Outliers
# =====================================================

plt.figure(figsize=(8,5))

sns.boxplot(x=df['Price (GBP)'])

plt.title("Boxplot of Book Prices")

plt.show()

# =====================================================
# STEP 12 - Correlation Heatmap
# =====================================================

plt.figure(figsize=(6,4))

sns.heatmap(
    df[['Price (GBP)', 'Rating (1-5)']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# =====================================================
# FINAL MESSAGE
# =====================================================

print("\n========== EDA COMPLETED SUCCESSFULLY ==========\n")