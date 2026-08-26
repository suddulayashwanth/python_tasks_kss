# Project Title: Scottish Hills Data Analysis
# Analyze Scottish Hills dataset using NumPy, Pandas and Matplotlib

# Import Required Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_folder = Path(__file__).parent
graphs_folder = project_folder / "Graphs"
graphs_folder.mkdir(exist_ok=True)

# Scenario 1: Data Loading and Preprocessing

# Load the dataset

df = pd.read_csv(project_folder / "scottish_hills.csv")

# Display first five rows

print("First 5 rows:")
print(df.head())

# Display column names

print("\nColumn names:")
print(df.columns)

# Convert Height column to numeric

df["Height"] = pd.to_numeric(
    df["Height"],
    errors="coerce"
)

# Create Region column

latitude_middle = df["Latitude"].median()
longitude_middle = df["Longitude"].median()

def assign_region(row):
    latitude = row["Latitude"]
    longitude = row["Longitude"]

    if latitude >= latitude_middle and longitude >= longitude_middle:
        return "North-East"
    elif latitude >= latitude_middle and longitude < longitude_middle:
        return "North-West"
    elif latitude < latitude_middle and longitude >= longitude_middle:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)

# Check missing values before cleaning

print("\nMissing values before cleaning:")
print(df[["Height", "Region"]].isnull().sum())

# Fill missing Height values with mean

height_mean = df["Height"].mean()
df["Height"] = df["Height"].fillna(height_mean)

# Fill missing Region values with mode

if not df["Region"].mode().empty:
    region_mode = df["Region"].mode()[0]
    df["Region"] = df["Region"].fillna(region_mode)

# Check missing values after cleaning

print("\nMissing values after cleaning:")
print(df[["Height", "Region"]].isnull().sum())

# Scenario 2: Height Line Graph

# Select Hill Name and Height columns

hill_data = df[["Hill Name", "Height"]]

# Select first ten rows

first_10_hills = hill_data.head(10)

# Convert Height into NumPy array

height_array = first_10_hills["Height"].to_numpy()

# Create line graph

plt.figure(figsize=(10, 6))
plt.plot(
    range(len(height_array)),
    height_array,
    marker="o",
    color="blue"
)

plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "hill_heights_line.png")
plt.close()

# Scenario 3: Tall Hills Bar Chart

# Filter hills with Height greater than 900

tall_hills = df[df["Height"] > 900]

# Count tall hills in each Region

region_counts = tall_hills["Region"].value_counts()

# Select top Regions

top_regions = region_counts.head(5)

print("\nTall hills in each Region:")
print(top_regions)

# Convert results into NumPy arrays

regions_array = top_regions.index.to_numpy()
counts_array = top_regions.to_numpy()

# Create bar chart

plt.figure(figsize=(10, 6))
plt.bar(
    regions_array,
    counts_array,
    color="orange"
)

plt.title("Number of Tall Hills Above 900 Metres per Region")
plt.xlabel("Region")
plt.ylabel("Number of Hills")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(graphs_folder / "tall_hills_bar.png")
plt.close()

# Scenario 4: Region Distribution Pie Chart

# Count hills in each Region

region_counts = df["Region"].value_counts()

# Select top five Regions

top_regions = region_counts.head(5)

# Prepare labels and values

region_labels = top_regions.index.to_numpy()
region_values = top_regions.to_numpy()

# Create pie chart

plt.figure(figsize=(8, 8))

plt.pie(
    region_values,
    labels=region_labels,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Distribution of Hills by Region")
plt.tight_layout()
plt.savefig(graphs_folder / "region_distribution.png")
plt.close()

# Scenario 5: Advanced Analysis and Multiple Graphs

# Create Height Category column

conditions = [
    df["Height"] >= 1000,
    df["Height"] >= 800
]

categories = [
    "Very High",
    "High"
]

df["Height Category"] = np.select(
    conditions,
    categories,
    default="Moderate"
)

# Convert Height column into NumPy array

all_heights = df["Height"].to_numpy()

# Calculate height differences

height_differences = np.diff(all_heights)

print("\nFirst 10 Height Differences:")
print(height_differences[:10])

# Scenario 5.1: Height Trend Line Graph

plt.figure(figsize=(12, 6))

plt.plot(
    range(len(all_heights)),
    all_heights,
    color="green"
)

plt.title("Height Trend of All Hills")
plt.xlabel("Hill Index")
plt.ylabel("Height")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "height_trend.png")
plt.close()

# Scenario 5.2: Height Category Stacked Bar Chart

category_region = pd.crosstab(
    df["Region"],
    df["Height Category"]
)

category_region.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Height Category Distribution per Region")
plt.xlabel("Region")
plt.ylabel("Number of Hills")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(graphs_folder / "height_category_stacked.png")
plt.close()

# Scenario 5.3: Height Distribution Histogram

plt.figure(figsize=(10, 6))

plt.hist(
    df["Height"],
    bins=10,
    color="purple",
    edgecolor="black"
)

plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(graphs_folder / "height_histogram.png")
plt.close()

# Scenario 5.4: Dataset Insights

# Find Region with highest average Height

tallest_region = (
    df.groupby("Region")["Height"]
    .mean()
    .idxmax()
)

# Find most common Height Category

common_category = (
    df["Height Category"]
    .value_counts()
    .idxmax()
)

# Calculate mean and median Heights

mean_height = df["Height"].mean()
median_height = df["Height"].median()

print("\nDataset Insights:")
print("Region with tallest hills:", tallest_region)
print("Most common Height Category:", common_category)
print("Mean Height:", round(mean_height, 2))
print("Median Height:", round(median_height, 2))

# Identify Height distribution pattern

if mean_height > median_height:
    print("Height distribution is positively skewed")
elif mean_height < median_height:
    print("Height distribution is negatively skewed")
else:
    print("Height distribution is symmetrical")

# End of Scottish Hills Data Analysis Project