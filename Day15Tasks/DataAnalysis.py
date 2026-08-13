import numpy as np

import pandas as pd

names = ["A", "B", "C", "D", "E"]

marks = np.random.randint(0, 101, size=5)

data = pd.DataFrame({"Name": names, "Marks": marks})

passing_students = data[data["Marks"] >= 50]

average = passing_students["Marks"].mean()

print("All students:")

print(data)

print("Passing students:")

for index, student in passing_students.iterrows():
    print(student["Name"], student["Marks"])

print("Average marks:", average)