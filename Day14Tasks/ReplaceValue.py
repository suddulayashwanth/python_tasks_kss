import pandas as pd

series = pd.Series([10, 50, 30, 80, 20])

updated_series = series.mask(series > 40, 0)

print(updated_series)