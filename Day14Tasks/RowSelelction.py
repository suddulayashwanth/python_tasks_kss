import pandas as pd

df = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]}, index=["x", "y", "z"])

selected_row = df.loc["y"]

print("Selected row:")

print(selected_row)

df = df.drop("x")

print("Updated DataFrame:")

print(df)