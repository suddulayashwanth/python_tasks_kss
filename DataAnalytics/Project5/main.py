# Project Title: Cars Data Analysis
# Analyze Cars dataset using NumPy, Pandas and Matplotlib

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

df = pd.read_csv(project_folder / "cardata.csv")

# Display first five rows

print("First 5 rows:")
print(df.head())

# Display last five rows

print("\nLast 5 rows:")
print(df.tail())

# Display column names

print("\nColumn names:")
print(df.columns)

# Display dataset shape

print("\nDataset shape:")
print(df.shape)

# Display column data types

print("\nColumn data types:")
print(df.dtypes)

# Convert columns to numeric

numeric_columns = [
    "Selling_Price",
    "Present_Price",
    "Kms_Driven",
    "Year"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Check missing values before cleaning

missing_columns = [
    "Selling_Price",
    "Present_Price",
    "Kms_Driven",
    "Fuel_Type"
]

print("\nMissing values before cleaning:")
print(df[missing_columns].isnull().sum())

# Fill Selling Price with mean

selling_price_mean = df["Selling_Price"].mean()

df["Selling_Price"] = df["Selling_Price"].fillna(
    selling_price_mean
)

# Fill Present Price with mean

present_price_mean = df["Present_Price"].mean()

df["Present_Price"] = df["Present_Price"].fillna(
    present_price_mean
)

# Fill Kms Driven with mean

kms_driven_mean = df["Kms_Driven"].mean()

df["Kms_Driven"] = df["Kms_Driven"].fillna(
    kms_driven_mean
)

# Fill Year with median

year_median = df["Year"].median()

df["Year"] = df["Year"].fillna(
    year_median
).astype(int)

# Fill Fuel Type with mode

if not df["Fuel_Type"].mode().empty:
    fuel_type_mode = df["Fuel_Type"].mode()[0]

    df["Fuel_Type"] = df["Fuel_Type"].fillna(
        fuel_type_mode
    )

# Check missing values after cleaning

print("\nMissing values after cleaning:")
print(df[missing_columns].isnull().sum())

# Convert columns into NumPy arrays

selling_price_array = df["Selling_Price"].to_numpy()
kms_driven_array = df["Kms_Driven"].to_numpy()

# Calculate Selling Price statistics

minimum_selling_price = np.min(selling_price_array)
maximum_selling_price = np.max(selling_price_array)
average_selling_price = np.mean(selling_price_array)

print("\nMinimum Selling Price:", minimum_selling_price)
print("Maximum Selling Price:", maximum_selling_price)
print("Average Selling Price:", average_selling_price)

# Scenario 2: Selling Price Trend Line Graph

# Select the first ten cars

first_10_cars = df[
    ["Car_Name", "Selling_Price"]
].head(10)

# Convert Selling Price into NumPy array

first_10_prices = first_10_cars[
    "Selling_Price"
].to_numpy()

# Create line graph

plt.figure(figsize=(10, 6))

plt.plot(
    range(len(first_10_prices)),
    first_10_prices,
    marker="o",
    color="darkblue"
)

plt.title("Selling Price Trend of First 10 Cars")
plt.xlabel("Car Index")
plt.ylabel("Selling Price")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "selling_price_line.png")
plt.close()

# Scenario 3: Expensive Cars Bar Chart

# Filter cars with Selling Price greater than 10

expensive_cars = df[
    df["Selling_Price"] > 10
]

# Count expensive cars by Fuel Type

expensive_fuel_counts = (
    expensive_cars.groupby("Fuel_Type")
    .size()
)

print("\nExpensive cars by Fuel Type:")
print(expensive_fuel_counts)

# Convert results into NumPy arrays

expensive_fuel_labels = (
    expensive_fuel_counts.index.to_numpy()
)

expensive_fuel_values = (
    expensive_fuel_counts.to_numpy()
)

# Create bar chart

plt.figure(figsize=(8, 5))

plt.bar(
    expensive_fuel_labels,
    expensive_fuel_values,
    color="skyblue",
    edgecolor="navy"
)

plt.title("Fuel Types of Expensive Cars")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig(graphs_folder / "expensive_car_analysis.png")
plt.close()

# Scenario 4: Fuel Type Distribution Pie Chart

# Count cars by Fuel Type

fuel_type_counts = df["Fuel_Type"].value_counts()

# Prepare labels and values

fuel_labels = fuel_type_counts.index.to_numpy()
fuel_values = fuel_type_counts.to_numpy()

# Create pie chart

plt.figure(figsize=(8, 8))

plt.pie(
    fuel_values,
    labels=fuel_labels,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Overall Fuel Type Distribution")
plt.tight_layout()
plt.savefig(graphs_folder / "fuel_type_distribution.png")
plt.close()

# Scenario 5: Present Price and Selling Price Scatter Plot

# Select required columns and remove missing values

price_data = df[
    ["Present_Price", "Selling_Price"]
].dropna()

# Select first 100 rows

sample_price_data = price_data.head(100)

# Convert columns into NumPy arrays

present_price_array = sample_price_data[
    "Present_Price"
].to_numpy()

sample_selling_price_array = sample_price_data[
    "Selling_Price"
].to_numpy()

# Create scatter plot

plt.figure(figsize=(10, 6))

plt.scatter(
    present_price_array,
    sample_selling_price_array,
    alpha=0.7,
    edgecolors="black"
)

plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(graphs_folder / "present_vs_selling_scatter.png")
plt.close()

# Calculate price correlation

price_correlation = np.corrcoef(
    present_price_array,
    sample_selling_price_array
)[0, 1]

print(
    "\nCorrelation between Present Price and Selling Price:",
    round(price_correlation, 2)
)

# Scenario 6: Car Age Category Bar Chart

# Create Car Age Category column

age_conditions = [
    df["Year"] >= 2015,
    df["Year"] >= 2010
]

age_categories = [
    "New",
    "Medium"
]

df["Car Age Category"] = np.select(
    age_conditions,
    age_categories,
    default="Old"
)

# Count cars in each Age Category

age_category_counts = (
    df["Car Age Category"]
    .value_counts()
)

# Arrange categories in correct order

category_order = [
    "New",
    "Medium",
    "Old"
]

age_category_counts = age_category_counts.reindex(
    category_order,
    fill_value=0
)

# Convert results into NumPy arrays

age_labels = age_category_counts.index.to_numpy()
age_values = age_category_counts.to_numpy()

# Create bar chart

plt.figure(figsize=(8, 5))

plt.bar(
    age_labels,
    age_values,
    color=["green", "orange", "red"]
)

plt.title("Car Distribution by Age Category")
plt.xlabel("Car Age Category")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig(graphs_folder / "car_age_category_bar.png")
plt.close()

# Scenario 7: Kms Driven Distribution Histogram

# Create histogram

plt.figure(figsize=(10, 6))

plt.hist(
    kms_driven_array,
    bins=15,
    color="purple",
    edgecolor="black"
)

plt.title("Kms Driven Distribution")
plt.xlabel("Kms Driven")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(graphs_folder / "kms_driven_histogram.png")
plt.close()

# Calculate Kms Driven statistics

average_kms = np.mean(kms_driven_array)
median_kms = np.median(kms_driven_array)

print("\nAverage Kms Driven:", round(average_kms, 2))
print("Median Kms Driven:", round(median_kms, 2))

if average_kms > median_kms:
    print(
        "Most cars have lower mileage with a few "
        "high-mileage cars"
    )
else:
    print(
        "Mileage is evenly distributed or concentrated "
        "in the higher range"
    )

# Scenario 8: Transmission-Wise Selling Price Comparison

# Calculate average Selling Price by Transmission

transmission_average = (
    df.groupby("Transmission")["Selling_Price"]
    .mean()
)

print("\nAverage Selling Price by Transmission:")
print(transmission_average)

# Convert results into NumPy arrays

transmission_labels = (
    transmission_average.index.to_numpy()
)

transmission_prices = (
    transmission_average.to_numpy()
)

# Create bar chart

plt.figure(figsize=(8, 5))

plt.bar(
    transmission_labels,
    transmission_prices,
    color="teal"
)

plt.title("Average Selling Price by Transmission")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price")
plt.tight_layout()
plt.savefig(graphs_folder / "transmission_selling_price.png")
plt.close()

# Scenario 9: Seller Type Analysis

# Count cars by Seller Type

seller_counts = (
    df["Seller_Type"]
    .value_counts()
    .sort_values(ascending=False)
)

# Convert results into NumPy arrays

seller_labels = seller_counts.index.to_numpy()
seller_values = seller_counts.to_numpy()

# Scenario 9.1: Seller Type Bar Chart

plt.figure(figsize=(8, 5))

plt.bar(
    seller_labels,
    seller_values,
    color=["green", "blue", "orange"]
)

plt.title("Seller Type Distribution")
plt.xlabel("Seller Type")
plt.ylabel("Number of Cars")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(graphs_folder / "seller_type_bar.png")
plt.close()

# Scenario 9.2: Seller Type Pie Chart

plt.figure(figsize=(8, 8))

plt.pie(
    seller_values,
    labels=seller_labels,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Seller Type Distribution")
plt.tight_layout()
plt.savefig(graphs_folder / "seller_type_pie.png")
plt.close()

# Find most common Seller Type

most_common_seller = seller_counts.idxmax()

print("\nMost Common Seller Type:", most_common_seller)

# Scenario 10: Advanced Analysis and Multiple Graphs

# Create Price Difference column

df["Price Difference"] = (
    df["Present_Price"] -
    df["Selling_Price"]
)

# Convert Price Difference into NumPy array

price_difference_array = df[
    "Price Difference"
].to_numpy()

# Calculate Selling Price changes

selling_price_changes = np.diff(
    selling_price_array
)

print("\nFirst 10 Selling Price Changes:")
print(selling_price_changes[:10])

# Calculate depreciation statistics

average_depreciation = np.mean(
    price_difference_array
)

maximum_depreciation = np.max(
    price_difference_array
)

minimum_depreciation = np.min(
    price_difference_array
)

print("\nAverage Depreciation:", average_depreciation)
print("Maximum Depreciation:", maximum_depreciation)
print("Minimum Depreciation:", minimum_depreciation)

# Scenario 10.1: Average Selling Price by Year

year_average = (
    df.groupby("Year")["Selling_Price"]
    .mean()
    .sort_index()
)

year_labels = year_average.index.to_numpy()
year_prices = year_average.to_numpy()

plt.figure(figsize=(10, 6))

plt.plot(
    year_labels,
    year_prices,
    marker="o",
    color="deeppink"
)

plt.title("Average Selling Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Selling Price")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(graphs_folder / "year_trend.png")
plt.close()

# Scenario 10.2: Average Selling Price by Fuel Type

fuel_average = (
    df.groupby("Fuel_Type")["Selling_Price"]
    .mean()
    .sort_values()
)

fuel_average_labels = fuel_average.index.to_numpy()
fuel_average_values = fuel_average.to_numpy()

plt.figure(figsize=(8, 5))

plt.bar(
    fuel_average_labels,
    fuel_average_values,
    color="royalblue"
)

plt.title("Average Selling Price by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Selling Price")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(graphs_folder / "fuel_bar.png")
plt.close()

# Scenario 10.3: Average Selling Price by Transmission

transmission_average = (
    df.groupby("Transmission")["Selling_Price"]
    .mean()
    .sort_values()
)

transmission_average_labels = (
    transmission_average.index.to_numpy()
)

transmission_average_values = (
    transmission_average.to_numpy()
)

plt.figure(figsize=(8, 5))

plt.bar(
    transmission_average_labels,
    transmission_average_values,
    color="teal"
)

plt.title("Average Selling Price by Transmission")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(graphs_folder / "transmission_bar.png")
plt.close()

# Scenario 10.4: Selling Price Distribution Histogram

plt.figure(figsize=(8, 5))

plt.hist(
    selling_price_array,
    bins=20,
    color="orangered",
    edgecolor="black"
)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(graphs_folder / "selling_price_histogram.png")
plt.close()

# Scenario 10.5: Dataset Insights

# Find Fuel Type with highest average Selling Price

highest_fuel_type = fuel_average.idxmax()

# Find Transmission with highest average Selling Price

highest_transmission = transmission_average.idxmax()

# Calculate mean and median Selling Price

mean_selling_price = np.mean(
    selling_price_array
)

median_selling_price = np.median(
    selling_price_array
)

# Calculate Car Age

current_year = 2026

df["Car Age"] = (
    current_year -
    df["Year"]
)

# Calculate relationship between Car Age and Selling Price

age_price_correlation = df[
    "Car Age"
].corr(df["Selling_Price"])

print("\nDataset Insights:")

print(
    "Fuel Type with highest average Selling Price:",
    highest_fuel_type
)

print(
    "Transmission with highest average Selling Price:",
    highest_transmission
)

if mean_selling_price > median_selling_price:
    print(
        "Most cars are concentrated in the lower "
        "Selling Price range"
    )
else:
    print(
        "Most cars are concentrated in the higher "
        "Selling Price range"
    )

if age_price_correlation < 0:
    print("Older cars tend to have lower Selling Prices")
else:
    print(
        "There is no strong negative relationship "
        "between Car Age and Selling Price"
    )

# End of Cars Data Analysis Project