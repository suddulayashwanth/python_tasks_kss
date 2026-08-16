import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Day": days, "Temperature": temps})

df["Category"] = np.where(df["Temperature"] > 30, "High", "Low")

temperature_counts = df["Category"].value_counts()

figure, axes = plt.subplots(2, 3, figsize=(15, 8))

axes = axes.flatten()

axes[0].plot(df["Day"], df["Temperature"], marker="o")

axes[0].set_title("Daily Temperature Trend")

axes[0].set_xlabel("Days")

axes[0].set_ylabel("Temperature")

axes[1].bar(df["Day"], df["Temperature"])

axes[1].set_title("Day-wise Temperature")

axes[1].set_xlabel("Days")

axes[1].set_ylabel("Temperature")

axes[2].pie(temperature_counts.values, labels=temperature_counts.index, autopct="%1.1f%%")

axes[2].set_title("High vs Low Temperature")

axes[3].hist(df["Temperature"], bins=5, edgecolor="black")

axes[3].set_title("Temperature Distribution")

axes[3].set_xlabel("Temperature")

axes[3].set_ylabel("Frequency")

axes[4].scatter(df.index, df["Temperature"])

axes[4].set_title("Day Index vs Temperature")

axes[4].set_xlabel("Day Index")

axes[4].set_ylabel("Temperature")

figure.delaxes(axes[5])

plt.tight_layout()

plt.show()