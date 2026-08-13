import random

import pandas as pd


class Student:
    def __init__(self, name, marks):
        self.name = name

        self.marks = marks

        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "F"


try:
    names = ["A", "B", "C", "D", "E"]

    marks = []

    for name in names:
        marks.append(random.randint(0, 100))

    students = []

    for name, mark in zip(names, marks):
        student = Student(name, mark)

        students.append(student)

    student_names = []

    student_marks = []

    student_grades = []

    for student in students:
        student_names.append(student.name)

        student_marks.append(student.marks)

        student_grades.append(student.grade)

    report = pd.DataFrame({
        "Name": student_names,
        "Marks": student_marks,
        "Grade": student_grades
    })

    average = report["Marks"].mean()

    standard_deviation = report["Marks"].std()

    highest_marks = report["Marks"].max()

    lowest_marks = report["Marks"].min()

    report.to_csv("exam_report.csv", index=False)

    print(report)

    print("Average marks:", average)

    print("Standard deviation:", standard_deviation)

    print("Highest marks:", highest_marks)

    print("Lowest marks:", lowest_marks)

    print("Report saved in exam_report.csv")

except (ValueError, TypeError, OSError) as error:
    print("Error:", error)