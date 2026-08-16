import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])

profit = np.array([50, 70, 60, 90, 80])

products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})

figure, axes = plt.subplots(2, 3, figsize=(15, 8))

axes = axes.flatten()

axes[0].plot(df["Product"], df["Sales"], marker="o")

axes[0].set_title("Sales Trend")

axes[0].set_xlabel("Products")

axes[0].set_ylabel("Sales")

axes[1].bar(df["Product"], df["Sales"])

axes[1].set_title("Product vs Sales")

axes[1].set_xlabel("Products")

axes[1].set_ylabel("Sales")

axes[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")

axes[2].set_title("Sales Contribution")

axes[3].hist(df["Profit"], bins=5, edgecolor="black")

axes[3].set_title("Profit Distribution")

axes[3].set_xlabel("Profit")

axes[3].set_ylabel("Frequency")

axes[4].scatter(df["Sales"], df["Profit"])

axes[4].set_title("Sales vs Profit")

axes[4].set_xlabel("Sales")

axes[4].set_ylabel("Profit")

figure.delaxes(axes[5])

plt.tight_layout()

plt.show()