import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

temperature_series = pd.Series(
    temps,
    index=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
)

print(temperature_series)

temperature_series.plot(marker="o")

plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.grid()

plt.show()