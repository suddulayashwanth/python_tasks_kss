# Project Title: IGN Data Analysis
# Analyze IGN dataset using NumPy, Pandas and Matplotlib

# Import Required Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

pd.set_option("future.no_silent_downcasting", True)

project_folder = Path(__file__).parent
graphs_folder = project_folder / "Graphs"
graphs_folder.mkdir(exist_ok=True)

# Scenario 1: Data Loading and Preprocessing

data = pd.read_csv(project_folder / "ign.csv")

# Display first five rows

print("First 5 rows:")
print(data.head())

# Display last five rows

print("\nLast 5 rows:")
print(data.tail())

# Display dataset shape

print("\nDataset shape:")
print(data.shape)

# Remove unnecessary column

data.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")

# Check missing values

print("\nMissing values before cleaning:")
print(data[["score", "genre", "platform"]].isnull().sum())

# Convert score column to numeric

data["score"] = pd.to_numeric(data["score"], errors="coerce")

# Fill missing score values with mean

average_score = data["score"].mean()
data["score"] = data["score"].fillna(average_score)

# Fill missing genre values with mode

if not data["genre"].mode().empty:
    genre_mode = data["genre"].mode()[0]
    data["genre"] = data["genre"].fillna(genre_mode)

# Fill missing platform values with mode

if not data["platform"].mode().empty:
    platform_mode = data["platform"].mode()[0]
    data["platform"] = data["platform"].fillna(platform_mode)

# Convert release date columns to integers

date_columns = ["release_year", "release_month", "release_day"]

for column in date_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")
    data[column] = data[column].fillna(0).astype(int)

# Convert score column to float

data["score"] = data["score"].astype(float)

# Check missing values after cleaning

print("\nMissing values after cleaning:")
print(data[["score", "genre", "platform"]].isnull().sum())

# Display column data types

print("\nColumn data types:")
print(data.dtypes)

# Scenario 2: Average Score Trend Line Graph

# Calculate average score for each year

grouped_year = data.groupby("release_year")["score"].mean()

print("\nAverage score for each year:")
print(grouped_year)

# Convert values into NumPy arrays

years = grouped_year.index.to_numpy()
average_scores = grouped_year.to_numpy()

# Create line graph

plt.figure(figsize=(10, 6))
plt.plot(years, average_scores, marker="o", color="blue")
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "avg_score_trend.png")
plt.close()

# Scenario 3: High-Rated Games by Platform Bar Chart

# Filter games with score greater than 7

high_rated_games = data[data["score"] > 7]

# Count high-rated games for each platform

platform_counts = high_rated_games.groupby("platform")["title"].count()

# Select top ten platforms

top_10_platforms = platform_counts.sort_values(ascending=False).head(10)

print("\nTop 10 platforms:")
print(top_10_platforms)

# Convert values into NumPy arrays

platform_names = top_10_platforms.index.to_numpy()
game_counts = top_10_platforms.to_numpy()

# Create bar chart

plt.figure(figsize=(12, 6))
plt.bar(platform_names, game_counts, color="orange")
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(graphs_folder / "top_platforms_bar.png")
plt.close()

# Scenario 4: Genre Distribution Pie Chart

# Count games for each genre

genre_counts = data["genre"].value_counts()

# Select top five genres

top_5_genres = genre_counts.head(5)

print("\nTop 5 genres:")
print(top_5_genres)

# Convert values into NumPy arrays

genre_names = top_5_genres.index.to_numpy()
genre_values = top_5_genres.to_numpy()

# Create pie chart

plt.figure(figsize=(8, 8))

plt.pie(
    genre_values,
    labels=genre_names,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Genre Distribution")
plt.tight_layout()
plt.savefig(graphs_folder / "genre_distribution.png")
plt.close()

# Scenario 5: Advanced Analysis and Multiple Graphs

# Create score category column

conditions = [
    data["score"] >= 9,
    data["score"] >= 7
]

categories = [
    "Excellent",
    "Good"
]

data["score_category"] = np.select(
    conditions,
    categories,
    default="Average"
)

# Convert editors choice values into numbers

data["editors_choice"] = data["editors_choice"].map({
    "Y": 1,
    "N": 0
})

# Calculate yearly average score

yearly_average = data.groupby("release_year")["score"].mean()

# Convert values into NumPy arrays

years = yearly_average.index.to_numpy()
average_scores = yearly_average.to_numpy()

# Calculate yearly score growth

score_growth = np.diff(average_scores)

print("\nYearly score growth:")
print(score_growth)

# Scenario 5.1: Score Trend Line Graph

plt.figure(figsize=(10, 6))
plt.plot(years, average_scores, marker="o", color="green")
plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True)
plt.tight_layout()
plt.savefig(graphs_folder / "score_trend.png")
plt.close()

# Scenario 5.2: Score Category Stacked Bar Chart

category_counts = data.pivot_table(
    index="release_year",
    columns="score_category",
    aggfunc="size",
    fill_value=0
)

category_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(14, 7)
)

plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(graphs_folder / "score_category_stacked.png")
plt.close()

# Scenario 5.3: Score Distribution Histogram

plt.figure(figsize=(10, 6))

plt.hist(
    data["score"],
    bins=20,
    color="purple",
    edgecolor="black"
)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(graphs_folder / "score_distribution.png")
plt.close()

# Scenario 5.4: Dataset Insights

# Find year with highest average score

highest_score_year = yearly_average.idxmax()
highest_average_score = yearly_average.max()

print(
    "\nYear with highest average score:",
    highest_score_year
)

print(
    "Highest average score:",
    round(highest_average_score, 2)
)

# Check overall score trend

if score_growth.mean() > 0:
    print("Overall trend: Scores increased over time")
else:
    print("Overall trend: Scores decreased or fluctuated over time")

# Compare editors choice with average score

editors_choice_average = data.groupby("editors_choice")["score"].mean()

print("\nAverage score based on editors choice:")
print(editors_choice_average)

if 0 in editors_choice_average.index and 1 in editors_choice_average.index:
    if editors_choice_average[1] > editors_choice_average[0]:
        print("Editors' Choice games generally have higher scores")
    else:
        print("Editors' Choice does not strongly relate to higher scores")

# End of IGN Data Analysis Project