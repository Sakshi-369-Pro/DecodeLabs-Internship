import pandas as pd
import os
print(os.listdir())

# Load Excel file
df = pd.read_excel("data.xlsx")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Fill text columns
text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].fillna("Unknown")

# Fill numeric columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(0)

print("Duplicates before:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicates after:", df.duplicated().sum())

df['CouponCode'] = df['CouponCode'].fillna("No Coupon")

print(df.isnull().sum())

print(df['PaymentMethod'].value_counts())
print(df['ReferralSource'].value_counts())

df.to_csv("cleaned_data.csv", index=False)