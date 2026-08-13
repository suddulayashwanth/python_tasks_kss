import pandas as pd

data = [
    [80, 90],
    [70, 60],
    [85, 95]
]

df = pd.DataFrame(data, columns=["Math", "Science"])

df["Total"] = df[["Math", "Science"]].sum(axis=1)

highest_index = df["Total"].idxmax()

highest_student = df.loc[highest_index]

print(df)

print("Student with the highest total:")

print(highest_student)

print("Student number:", highest_index + 1)