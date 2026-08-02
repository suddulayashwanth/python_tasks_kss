subjects = ("Math", "Science", "English")

student_names = set()
student_records = {}


def recursive_total(marks, index=0):
    if index == len(marks):
        return 0

    return marks[index] + recursive_total(marks, index + 1)


def add_student():
    name = input("Enter student name: ").strip()
    marks = []

    try:
        for subject in subjects:
            value = float(input(f"Enter marks for {subject}: "))

            if value.is_integer():
                value = int(value)

            marks.append(value)

        student_names.add(name)
        student_records[name] = marks

        print("Student added successfully.")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

    except TypeError:
        print("Marks data type error.")


def display_students():
    if not student_names:
        print("No student records available.")
        return

    for name in student_names:
        print(f"{name} : {student_records[name]}")


def calculate_average():
    name = input(
        "Enter student name to calculate average: "
    ).strip()

    try:
        if name not in student_records:
            raise NameError

        marks = student_records[name]

        if not isinstance(marks, list):
            raise TypeError

        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise TypeError

        total = recursive_total(marks)
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")