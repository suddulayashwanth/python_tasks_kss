import pandas as pd

df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90]})

df["Status"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 50 else "Fail")

passed_students = df[df["Status"] == "Pass"]

average_marks = passed_students["Marks"].mean()

print(df)

print("Passed students:")

print(passed_students)

print("Average marks of passed students:", average_marks)