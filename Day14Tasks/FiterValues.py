import pandas as pd

series = pd.Series([10, 25, 30, 15, 40])

filtered_values = series[series > 20]

print(filtered_values)