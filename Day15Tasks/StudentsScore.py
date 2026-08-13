import pandas as pd

student_data = [("A", 45), ("B", 75), ("C", 60), ("D", 40)]

students = dict(student_data)

data = pd.DataFrame(list(students.items()), columns=["Name", "Marks"])

above_50 = data[data["Marks"] > 50]

average = data["Marks"].mean()

above_50.to_csv("student_results.txt", sep="\t", index=False)

with open("student_results.txt", "a") as file:
    file.write(f"\nAverage marks: {average}")

print("Students scoring above 50:")

print(above_50)

print("Average marks:", average)