import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv('../data/raw_data.csv')

print("===== BEFORE CLEANING =====")
print("Shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean column names (remove extra spaces, standardize)
df.columns = df.columns.str.strip()

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Text columns -> fill with 'Unknown'
text_cols = ['First Name', 'Last Name', 'Department', 'Region', 'Status', 'Email', 'Phone']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# Numeric columns -> fill with median
numeric_cols = ['Age', 'Salary', 'Performance Score']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(df[col].median())

# 3. Fix data types
if 'Join Date' in df.columns:
    df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')

if 'Employee ID' in df.columns:
    df['Employee ID'] = df['Employee ID'].astype(str).str.strip()

# 4. Fix inconsistent text values (casing, whitespace)
for col in ['First Name', 'Last Name', 'Department', 'Region', 'Status']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

if 'Email' in df.columns:
    df['Email'] = df['Email'].astype(str).str.strip().str.lower()

# Standardize Remote Work column (Yes/No, True/False, etc.)
if 'Remote Work' in df.columns:
    df['Remote Work'] = df['Remote Work'].astype(str).str.strip().str.lower()
    df['Remote Work'] = df['Remote Work'].replace({
        'yes': 'Yes', 'y': 'Yes', 'true': 'Yes', '1': 'Yes',
        'no': 'No', 'n': 'No', 'false': 'No', '0': 'No'
    })

# Remove rows where Employee ID is missing (critical field)
if 'Employee ID' in df.columns:
    df = df.dropna(subset=['Employee ID'])

print("\n===== AFTER CLEANING =====")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Save cleaned data
df.to_csv('../data/cleaned_data.csv', index=False)
print("\nCleaned data saved to data/cleaned_data.csv")