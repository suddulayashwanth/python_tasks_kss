import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Scenario 1 Basic Data Loading & Cleaning

df = pd.read_csv("railway_gauges.csv")
print(df.head())
print(df.columns)

print(df.isnull().sum())

df = df.fillna(0)
print(df.isnull().sum())

gauge_columns = [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge",
    "Total"
]

for column in gauge_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

print(df.dtypes)    

# Scenario 2: Simple Visualization

data = df[["Year", "Total"]]

print(data.head())

plt.plot(data["Year"], data["Total"])

plt.title("Total Railway Tracks Over Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")

plt.xticks(rotation=60)

plt.savefig("Graphs/total_railway_growth.png")
plt.show()

# Scenario 3: Filtering + Bar Chart

df["Start Year"] = df["Year"].str[:4].astype(int)

recent = df[df["Start Year"] > 2000]

print(recent)

gauge_data = recent[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print(gauge_data)

gauge_data.plot(
    x="Year",
    kind="bar",
    figsize=(12, 6)
)

plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.xticks(rotation=60)
plt.legend(title="Gauge Type")

plt.savefig("Graphs/gauge_comparison_after_2000.png")

plt.show()

gauge_totals = recent[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print(gauge_totals)

dominant_gauge = gauge_totals.idxmax()

print("Dominant gauge:", dominant_gauge)

# Scenario 4: Latest Year Gauge Composition

latest = df.iloc[-1]

print(latest)

gauge_composition = latest[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print(gauge_composition)

gauge_composition.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)

plt.title("Railway Gauge Composition in Latest Year")
plt.ylabel("")

plt.savefig("Graphs/gauge_composition.png")

plt.show()

# Find dominant gauge in latest year
plt.savefig("Graphs/gauge_composition.png")

latest_values = pd.to_numeric(df.iloc[-1][gauge_columns])
latest_dominant = latest_values.idxmax()
print("Dominant gauge in latest year:", latest_dominant)

gauge_percentages = (
    gauge_composition / gauge_composition.sum()
) * 100

print("Gauge percentage share:")
print(gauge_percentages)

# Scenario 5: Advanced Analysis

df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

print(
    df[
        [
            "Year",
            "% Broad Gauge",
            "% Metre Gauge",
            "% Narrow Gauge"
        ]
    ].head()
)

# Calculate yearly growth using NumPy

total_tracks = df["Total"].to_numpy()

growth = np.diff(total_tracks)

print("Yearly growth:")
print(growth)

# Find highest growth
highest_growth = growth.max()

highest_growth_index = growth.argmax()

highest_growth_year = df["Year"].iloc[highest_growth_index + 1]

print("Highest yearly growth:", highest_growth)
print("Year with highest growth:", highest_growth_year)

# Find years with decline

decline_indices = np.where(growth < 0)[0]

decline_years = df["Year"].iloc[decline_indices + 1]

print("Years with decline:")
print(decline_years)

# Line graph for all gauges

plt.figure(figsize=(12, 6))

plt.plot(df["Year"], df["Broad Gauge"], label="Broad Gauge")
plt.plot(df["Year"], df["Metre Gauge"], label="Metre Gauge")
plt.plot(df["Year"], df["Narrow Gauge"], label="Narrow Gauge")

plt.title("Railway Gauge Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")

plt.xticks(rotation=60)
plt.legend()

plt.savefig("Graphs/all_gauge_trends.png")
plt.show()

# Stacked bar chart for gauge composition

plt.figure(figsize=(14, 7))

plt.bar(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.bar(
    df["Year"],
    df["Metre Gauge"],
    bottom=df["Broad Gauge"],
    label="Metre Gauge"
)

plt.bar(
    df["Year"],
    df["Narrow Gauge"],
    bottom=df["Broad Gauge"] + df["Metre Gauge"],
    label="Narrow Gauge"
)

plt.title("Railway Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")

plt.xticks(rotation=60)
plt.legend()

plt.savefig("Graphs/gauge_composition_stacked.png")

plt.show()

# Final analysis

latest_percentages = df.iloc[-1][
    ["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]
]

print("Latest year gauge percentages:")
print(latest_percentages)

dominant_percentage = latest_percentages.idxmax()

print("Dominant gauge based on latest percentage:",
      dominant_percentage)

if dominant_percentage == "% Broad Gauge":
    print("Conclusion: The railway system is strongly dominated by Broad Gauge.")
else:
    print("Conclusion: The railway system is not dominated by Broad Gauge.")

    # Scenario 4: Total Gauge Contribution Across All Years

gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("Total gauge contribution across all years:")
print(gauge_totals)

gauge_totals.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)

plt.title("Railway Gauge Contribution Across All Years")
plt.ylabel("")

plt.savefig("Graphs/gauge_total_contribution.png")

plt.show()

print("Gauge contributing the most:", gauge_totals.idxmax())