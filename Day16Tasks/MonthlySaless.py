import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({"Month": months, "Sales": sales})

figure, axes = plt.subplots(2, 3, figsize=(15, 8))

axes = axes.flatten()

axes[0].plot(df["Month"], df["Sales"], marker="o")

axes[0].set_title("Sales Trend")

axes[0].set_xlabel("Months")

axes[0].set_ylabel("Sales")

axes[1].bar(df["Month"], df["Sales"])

axes[1].set_title("Month-wise Sales")

axes[1].set_xlabel("Months")

axes[1].set_ylabel("Sales")

axes[2].pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")

axes[2].set_title("Monthly Sales Contribution")

axes[3].hist(df["Sales"], bins=5, edgecolor="black")

axes[3].set_title("Sales Distribution")

axes[3].set_xlabel("Sales")

axes[3].set_ylabel("Frequency")

axes[4].scatter(df.index, df["Sales"])

axes[4].set_title("Month Index vs Sales")

axes[4].set_xlabel("Month Index")

axes[4].set_ylabel("Sales")

figure.delaxes(axes[5])

plt.tight_layout()

plt.show()