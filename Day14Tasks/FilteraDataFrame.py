import pandas as pd

names = ["A", "B", "C"]

marks = [80, 90, 70]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

filtered_students = df[df["Marks"] > 75]

print(df)

print("Students with marks above 75:")

print(filtered_students)