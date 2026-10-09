import pandas as pd
import numpy as np

# ==============================================
#  HEALTHCARE READMISSION ANALYSIS
# ==============================================

# Load the data
df = pd.read_csv("diabetic_data.csv")

print("✅ Data loaded successfully!")
print(f"Total rows: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")

# ==============================================
#  DATA CLEANING
# ==============================================
print("\n🧹 Starting data cleaning...")

# 1. Replace '?' with proper missing value marker
df = df.replace('?', pd.NA)

# 2. Drop columns with too many missing values
# Columns like weight, payer_code have over 90% missing
cols_to_drop = ['weight', 'payer_code', 'medical_specialty']
df = df.drop(columns=cols_to_drop)
print(f"✅ Dropped columns with mostly missing data: {cols_to_drop}")

# 3. Remove records with invalid/missing gender
invalid_gender = df[df['gender'] == 'Unknown/Invalid'].shape[0]
df = df[df['gender'] != 'Unknown/Invalid']
print(f"✅ Removed {invalid_gender} records with unknown gender")

# 4. Remove duplicate patient encounters if any
initial_rows = df.shape[0]
df = df.drop_duplicates(subset=['patient_nbr', 'encounter_id'], keep='first')
duplicates_removed = initial_rows - df.shape[0]
print(f"✅ Removed {duplicates_removed} duplicate records")

# 5. Show remaining missing values summary
missing = df.isnull().sum()
print("\n📋 Remaining missing values per column:")
print(missing[missing > 0].sort_values(ascending=False).head(10))

print("\n✅ Cleaning complete!")
print(f"Final data shape: {df.shape[0]} rows, {df.shape[1]} columns")

# ==============================================
#  PART 1 — OVERVIEW & READMISSION RATES
# ==============================================
print("\n" + "="*50)
print("PART 1 — OVERALL READMISSION STATUS")
print("="*50)

print("\nReadmission Overview:")
print(df['readmitted'].value_counts())

# ==============================================
#  PART 2 — DEMOGRAPHICS & HOSPITAL STAY
# ==============================================
print("\n" + "="*50)
print("PART 2 — DEMOGRAPHICS & STAY LENGTH")
print("="*50)

print("\nReadmissions by Gender:")
gender_readmit = df.groupby(['gender', 'readmitted']).size().unstack(fill_value=0)
print(gender_readmit)

print("\nAverage Length of Stay by Readmission Status:")
stay_length = df.groupby('readmitted')['time_in_hospital'].mean().round(1)
print(stay_length)

# ==============================================
#  PART 3 — MEDICATIONS
# ==============================================
print("\n" + "="*50)
print("PART 3 — MEDICATIONS & READMISSIONS")
print("="*50)

print("\nReadmission Rates — Medication Changed vs Not Changed:")
med_change = df.groupby(['change', 'readmitted']).size().unstack(fill_value=0)
print(med_change)

print("\nAverage Number of Medications by Readmission:")
meds = df.groupby('readmitted')['num_medications'].mean().round(1)
print(meds)

print("\n✅ Analysis complete!")
# ==============================================
#  SAVE THE CLEANED DATASET
# ==============================================

# Save as CSV — easy to open in Excel or other tools
df.to_csv("diabetic_data_cleaned.csv", index=False)
print("✅ Cleaned dataset saved as: diabetic_data_cleaned.csv")
print(f"   Saved: {df.shape[0]} rows, {df.shape[1]} columns")