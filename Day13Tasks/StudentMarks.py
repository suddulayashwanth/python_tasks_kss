import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

total_marks = np.sum(marks, axis=1)

class_average = np.mean(total_marks)

above_average_indices = np.where(total_marks > class_average)[0]

student_numbers = above_average_indices + 1

print("Total marks of each student:", total_marks)
print("Class average:", class_average)
print("Students above class average:", student_numbers)