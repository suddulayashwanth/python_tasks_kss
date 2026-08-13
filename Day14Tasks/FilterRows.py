import pandas as pd

data = [
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
]

df = pd.DataFrame(data, columns=["Sales", "Profit"])

filtered_rows = df[df["Sales"] > 100]

average_profit = filtered_rows["Profit"].mean()

print(df)

print("Rows where Sales is greater than 100:")

print(filtered_rows)

print("Average profit:", average_profit)