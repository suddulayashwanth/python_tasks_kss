import pandas as pd

S1 = pd.Series([10, 20, 30],
    index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25],
    index=["apple", "banana", "cherry"])
result = S1.add(S2)
print(result)
print("Total sales:", result.sum())