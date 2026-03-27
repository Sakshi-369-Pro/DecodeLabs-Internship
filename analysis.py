import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# -----------------------------
# BASIC ANALYSIS
# -----------------------------

print("Total Revenue:", df['TotalPrice'].sum())
print("Average Order Value:", df['TotalPrice'].mean())

print("\nPayment Method Distribution:")
print(df['PaymentMethod'].value_counts())

print("\nTop Products:")
print(df['Product'].value_counts().head())

print("\nReferral Sources:")
print(df['ReferralSource'].value_counts())

# -----------------------------
# TIME ANALYSIS
# -----------------------------

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

print("\nOrders per Month:")
print(df['Month'].value_counts().sort_index())

# -----------------------------
# VISUALIZATION
# -----------------------------

# Payment Method Chart
df['PaymentMethod'].value_counts().plot(kind='bar')
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

# Referral Source Chart
df['ReferralSource'].value_counts().plot(kind='bar')
plt.title("Referral Source Distribution")
plt.xlabel("Source")
plt.ylabel("Count")
plt.show()