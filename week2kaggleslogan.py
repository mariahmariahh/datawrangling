import pandas as pd
import numpy as np

raw=pd.read_csv('AB_NYC_2019.csv')

df=pd.DataFrame(raw)
df.fillna(0,inplace=True)
df.drop_duplicates()
print(df)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'AB_NYC_2019.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Data Cleaning
data_cleaned = data.dropna(subset=['name', 'host_name'])
data_cleaned['reviews_per_month'] = data_cleaned['reviews_per_month'].fillna(0)
data_cleaned['last_review'] = pd.to_datetime(data_cleaned['last_review'], errors='coerce')
data_cleaned = data_cleaned.drop_duplicates()
data_cleaned = data_cleaned[(data_cleaned['price'] > 0) & (data_cleaned['price'] <= 1000)]
data_cleaned = data_cleaned[data_cleaned['minimum_nights'] <= 365]

# Feature Extraction
data_cleaned['last_review_year'] = data_cleaned['last_review'].dt.year
data_cleaned['last_review_month'] = data_cleaned['last_review'].dt.month

# Aggregations for Visualization
room_type_popularity = data_cleaned['room_type'].value_counts()
neighbourhood_group_popularity = data_cleaned['neighbourhood_group'].value_counts()
price_by_room_type = data_cleaned.groupby('room_type')['price'].mean()
monthly_reviews = data_cleaned.groupby(['last_review_year', 'last_review_month'])['reviews_per_month'].sum().reset_index()

# Generate and Save Graphs
# Room Type Popularity
plt.figure(figsize=(8, 5))
sns.barplot(x=room_type_popularity.index, y=room_type_popularity.values, palette="viridis")
plt.title("Room Type Popularity", fontsize=14)
plt.xlabel("Room Type", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.savefig('room_type_popularity.png')
plt.close()

# Neighborhood Group Popularity
plt.figure(figsize=(8, 5))
sns.barplot(x=neighbourhood_group_popularity.index, y=neighbourhood_group_popularity.values, palette="muted")
plt.title("Neighborhood Group Popularity", fontsize=14)
plt.xlabel("Neighborhood Group", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.savefig('neighbourhood_group_popularity.png')
plt.close()

# Price by Room Type
plt.figure(figsize=(8, 5))
sns.barplot(x=price_by_room_type.index, y=price_by_room_type.values, palette="coolwarm")
plt.title("Average Price by Room Type", fontsize=14)
plt.xlabel("Room Type", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.savefig('price_by_room_type.png')
plt.close()

# Monthly Reviews Trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_reviews, x='last_review_month', y='reviews_per_month', hue='last_review_year', palette="tab10")
plt.title("Monthly Reviews Over Time", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Reviews Per Month", fontsize=12)
plt.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('monthly_reviews_trend.png')
plt.close()

print("Graphs saved as 'room_type_popularity.png', 'neighbourhood_group_popularity.png', 'price_by_room_type.png', and 'monthly_reviews_trend.png'.")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'AB_NYC_2019.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Data Cleaning
data_cleaned = data.dropna(subset=['name', 'host_name'])
data_cleaned['reviews_per_month'] = data_cleaned['reviews_per_month'].fillna(0)
data_cleaned['last_review'] = pd.to_datetime(data_cleaned['last_review'], errors='coerce')
data_cleaned = data_cleaned.drop_duplicates()
data_cleaned = data_cleaned[(data_cleaned['price'] > 0) & (data_cleaned['price'] <= 1000)]
data_cleaned = data_cleaned[data_cleaned['minimum_nights'] <= 365]

# Feature Extraction
data_cleaned['last_review_year'] = data_cleaned['last_review'].dt.year
data_cleaned['last_review_month'] = data_cleaned['last_review'].dt.month

# Aggregations for Visualization
room_type_popularity = data_cleaned['room_type'].value_counts()
neighbourhood_group_popularity = data_cleaned['neighbourhood_group'].value_counts()
price_by_room_type = data_cleaned.groupby('room_type')['price'].mean()
monthly_reviews = data_cleaned.groupby(['last_review_year', 'last_review_month'])['reviews_per_month'].sum().reset_index()

# Generate and Save Graphs
# Room Type Popularity
plt.figure(figsize=(8, 5))
sns.barplot(x=room_type_popularity.index, y=room_type_popularity.values, palette="viridis")
plt.title("Room Type Popularity", fontsize=14)
plt.xlabel("Room Type", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.savefig('room_type_popularity.png')
plt.close()

# Neighborhood Group Popularity
plt.figure(figsize=(8, 5))
sns.barplot(x=neighbourhood_group_popularity.index, y=neighbourhood_group_popularity.values, palette="muted")
plt.title("Neighborhood Group Popularity", fontsize=14)
plt.xlabel("Neighborhood Group", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.savefig('neighbourhood_group_popularity.png')
plt.close()

# Price by Room Type
plt.figure(figsize=(8, 5))
sns.barplot(x=price_by_room_type.index, y=price_by_room_type.values, palette="coolwarm")
plt.title("Average Price by Room Type", fontsize=14)
plt.xlabel("Room Type", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.savefig('price_by_room_type.png')
plt.close()

# Monthly Reviews Trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_reviews, x='last_review_month', y='reviews_per_month', hue='last_review_year', palette="tab10")
plt.title("Monthly Reviews Over Time", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Reviews Per Month", fontsize=12)
plt.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('monthly_reviews_trend.png')
plt.close()

print("Graphs saved as 'room_type_popularity.png', 'neighbourhood_group_popularity.png', 'price_by_room_type.png', and 'monthly_reviews_trend.png'.")
