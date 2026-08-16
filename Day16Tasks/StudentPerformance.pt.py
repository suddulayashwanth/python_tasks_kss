import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])

students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student": students, "Marks": marks})

df["Result"] = np.where(df["Marks"] > 50, "Pass", "Fail")

result_counts = df["Result"].value_counts()

figure, axes = plt.subplots(2, 3, figsize=(15, 8))

axes = axes.flatten()

axes[0].plot(df["Student"], df["Marks"], marker="o")

axes[0].set_title("Marks Trend")

axes[0].set_xlabel("Students")

axes[0].set_ylabel("Marks")

axes[1].bar(df["Student"], df["Marks"])

axes[1].set_title("Student vs Marks")

axes[1].set_xlabel("Students")

axes[1].set_ylabel("Marks")

axes[2].pie(result_counts.values, labels=result_counts.index, autopct="%1.1f%%")

axes[2].set_title("Pass vs Fail")

axes[3].hist(df["Marks"], bins=5, edgecolor="black")

axes[3].set_title("Marks Distribution")

axes[3].set_xlabel("Marks")

axes[3].set_ylabel("Frequency")

axes[4].scatter(df.index, df["Marks"])

axes[4].set_title("Index vs Marks")

axes[4].set_xlabel("Index")

axes[4].set_ylabel("Marks")

figure.delaxes(axes[5])

plt.tight_layout()

plt.show()