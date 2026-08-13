import pandas as pd

series = pd.Series(
    [10, pd.NA, 30, pd.NA, 50],
    dtype="Float64"
)

mean_value = series.mean()

updated_series = series.fillna(mean_value)

print("Mean:", mean_value)

print(updated_series)