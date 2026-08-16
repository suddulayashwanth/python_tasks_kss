import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

series = pd.Series(data)

average = series.mean()

cleaned_series = series.fillna(average)

above_average = cleaned_series[cleaned_series > average]

print("Average:", average)

print("Cleaned data:")

print(cleaned_series)

figure, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(cleaned_series.index, cleaned_series.values, marker="o")

axes[0].set_title("Cleaned Data")

axes[0].set_xlabel("Index")

axes[0].set_ylabel("Values")

axes[0].grid(True)

axes[1].bar(above_average.index.astype(str), above_average.values)

axes[1].set_title("Values Above Average")

axes[1].set_xlabel("Index")

axes[1].set_ylabel("Values")

plt.tight_layout()

plt.show()