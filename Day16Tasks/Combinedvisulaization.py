import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])

products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Product": products, "Sales": sales})

figure, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(df["Product"], df["Sales"], marker="o")

axes[0].set_title("Sales Trend")

axes[0].set_xlabel("Products")

axes[0].set_ylabel("Sales")

axes[1].bar(df["Product"], df["Sales"])

axes[1].set_title("Sales Comparison")

axes[1].set_xlabel("Products")

axes[1].set_ylabel("Sales")

axes[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")

axes[2].set_title("Sales Distribution")

plt.tight_layout()

plt.show()