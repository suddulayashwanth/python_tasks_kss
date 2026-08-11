marks = [50, 60, 70, 80]

backup = marks

marks[0] = 90

print("Marks:", marks)
print("Backup:", backup)

print("Both changed because marks and backup refer to the same list.")