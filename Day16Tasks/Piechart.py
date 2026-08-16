import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

categories = np.where(scores > 50, "Pass", "Fail")

category_counts = pd.Series(categories).value_counts()

print(category_counts)

plt.pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%")

plt.title("Pass vs Fail")

plt.axis("equal")

plt.show()