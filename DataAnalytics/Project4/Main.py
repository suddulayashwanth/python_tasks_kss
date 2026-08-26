# Project Title: House Sales Data Analysis
# Analyze House Sales dataset using NumPy, Pandas and Matplotlib

# Import Required Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_folder = Path(__file__).parent
graphs_folder = project_folder / "Graphs"
graphs_folder.mkdir(exist_ok=True)

# Scenario 1: Data Loading and Basic Cleaning

# Load the dataset

df = pd.read_csv(project_folder / "kc_house_data.csv")

# Display first five rows

print("First 5 rows:")
print(df.head())

# Display column names

print("\nColumn names:")
print(df.columns)

# Select numeric columns

numeric_columns = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "price"
]

# Convert columns to numeric

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Check missing values before cleaning

print("\nMissing values before cleaning:")
print(df[numeric_columns].isnull().sum())

# Fill missing bedrooms with mode

if not df["bedrooms"].mode().empty:
    bedroom_mode = df["bedrooms"].mode()[0]
    df["bedrooms"] = df["bedrooms"].fillna(bedroom_mode)

# Fill missing bathrooms with mean

bathroom_mean = df["bathrooms"].mean()
df["bathrooms"] = df["bathrooms"].fillna(bathroom_mean)

# Fill missing sqft_living with mean

sqft_living_mean = df["sqft_living"].mean()
df["sqft_living"] = df["sqft_living"].fillna(sqft_living_mean)

# Fill missing price with mean

price_mean = df["price"].mean()
df["price"] = df["price"].fillna(price_mean)

# Convert bedrooms to integer

df["bedrooms"] = df["bedrooms"].round().astype(int)

# Check missing values after cleaning

print("\nMissing values after cleaning:")
print(df[numeric_columns].isnull().sum())

# Scenario 2: House Price Line Graph

# Select id and price columns

line_data = df[["id", "price"]].head(10)

# Convert price into NumPy array

price_array = line_data["price"].to_numpy()

# Create line graph

plt.figure(figsize=(10, 6))

plt.plot(
    range(len(price_array)),
    price_array,
    marker="o",
    color="darkblue"
)

plt.title("House Prices of First 10 Records")
plt.xlabel("Index")
plt.ylabel("Price")
plt.ticklabel_format(style="plain", axis="y")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "house_prices_line.png")
plt.close()

# Scenario 3: Expensive Houses Bar Chart

# Filter houses with price greater than 1000000

expensive_houses = df[df["price"] > 1000000]

# Count expensive houses for each bedroom category

bedroom_counts = expensive_houses["bedrooms"].value_counts()

# Select top five bedroom categories

top_bedrooms = bedroom_counts.head(5)

print("\nTop bedroom categories for expensive houses:")
print(top_bedrooms)

# Convert results into NumPy arrays

bedroom_array = top_bedrooms.index.to_numpy()
house_count_array = top_bedrooms.to_numpy()

# Create bar chart

plt.figure(figsize=(10, 6))

plt.bar(
    bedroom_array,
    house_count_array,
    color="skyblue",
    edgecolor="navy"
)

plt.title("Expensive Houses by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Number of Houses")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(graphs_folder / "expensive_houses_bar.png")
plt.close()

# Scenario 4: Bedroom Distribution Pie Chart

# Count houses for each bedroom category

bedroom_counts = df["bedrooms"].value_counts()

# Select top five bedroom categories

top_5_bedrooms = bedroom_counts.head(5)

# Prepare labels and values

bedroom_labels = [
    f"{int(bedroom)} Bedrooms"
    for bedroom in top_5_bedrooms.index
]

bedroom_values = top_5_bedrooms.to_numpy()

# Create pie chart

plt.figure(figsize=(10, 7))

plt.pie(
    bedroom_values,
    labels=bedroom_labels,
    autopct="%1.1f%%",
    startangle=140,
    shadow=True
)

plt.title("Top 5 Bedroom Categories")
plt.axis("equal")
plt.tight_layout()
plt.savefig(graphs_folder / "bedroom_distribution.png")
plt.close()

# Scenario 5: Advanced Analysis and Multiple Graphs

# Create Price Category column

conditions = [
    df["price"] >= 1000000,
    df["price"] >= 500000
]

price_categories = [
    "Luxury",
    "Mid Range"
]

df["Price Category"] = np.select(
    conditions,
    price_categories,
    default="Affordable"
)

print("\nPrice Category counts:")
print(df["Price Category"].value_counts())

# Convert price column into NumPy array

all_prices = df["price"].to_numpy()

# Calculate price differences

price_differences = np.diff(all_prices)

print("\nFirst 10 Price Differences:")
print(price_differences[:10])

# Scenario 5.1: House Price Trend Line Graph

plt.figure(figsize=(12, 6))

plt.plot(
    range(len(all_prices)),
    all_prices,
    color="green"
)

plt.title("House Price Trend")
plt.xlabel("House Index")
plt.ylabel("Price")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.savefig(graphs_folder / "price_trend.png")
plt.close()

# Scenario 5.2: Price Category Stacked Bar Chart

# Remove unrealistic bedroom values for analysis

analysis_data = df[
    (df["bedrooms"] >= 1) &
    (df["bedrooms"] <= 10)
].copy()

# Count Price Categories for each bedroom category

stacked_data = pd.crosstab(
    analysis_data["bedrooms"],
    analysis_data["Price Category"]
)

# Select top five bedroom categories

top_bedroom_categories = (
    analysis_data["bedrooms"]
    .value_counts()
    .head(5)
    .index
)

stacked_data = stacked_data.loc[
    stacked_data.index.isin(top_bedroom_categories)
]

stacked_data = stacked_data.sort_index()

# Create stacked bar chart

stacked_data.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Price Category Distribution by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Number of Houses")
plt.xticks(rotation=0)
plt.legend(title="Price Category")
plt.tight_layout()
plt.savefig(graphs_folder / "price_category_stacked.png")
plt.close()

# Scenario 5.3: House Price Distribution Histogram

plt.figure(figsize=(10, 6))

plt.hist(
    df["price"],
    bins=30,
    color="gold",
    edgecolor="black"
)

plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.ticklabel_format(style="plain", axis="x")
plt.tight_layout()
plt.savefig(graphs_folder / "price_histogram.png")
plt.close()

# Scenario 5.4: Dataset Insights

# Find bedroom category with highest average price

average_price_by_bedroom = (
    analysis_data.groupby("bedrooms")["price"]
    .mean()
)

most_expensive_bedroom = average_price_by_bedroom.idxmax()

# Find most common Price Category

most_common_category = (
    df["Price Category"]
    .value_counts()
    .idxmax()
)

# Calculate mean and median prices

mean_price = df["price"].mean()
median_price = df["price"].median()

print("\nDataset Insights:")
print(
    "Bedroom category with highest average price:",
    most_expensive_bedroom
)

print(
    "Most common Price Category:",
    most_common_category
)

# Identify price distribution pattern

if mean_price > median_price:
    print(
        "Price distribution is right-skewed with most houses "
        "concentrated in the lower price range"
    )
elif mean_price < median_price:
    print("Price distribution is left-skewed")
else:
    print("Price distribution is approximately symmetrical")

# End of House Sales Data Analysis Project