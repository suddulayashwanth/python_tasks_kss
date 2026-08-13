import pandas as pd


class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id

        self.name = name

        self.salary = salary

    def display(self):
        print(self.employee_id, self.name, self.salary)


employees = {}

employee_records = []

try:
    number_of_employees = int(input("Enter number of employees: "))

except ValueError:
    print("Invalid employee count")

    number_of_employees = 0

for i in range(number_of_employees):
    employee_id = input("Enter employee ID: ")

    name = input("Enter employee name: ")

    try:
        salary = float(input("Enter salary: "))

        if salary < 0:
            raise ValueError

        employee = Employee(employee_id, name, salary)

        employees[employee_id] = employee

        employee_records.append({"ID": employee_id, "Name": name, "Salary": salary})

    except ValueError:
        print("Invalid salary input")

employee_data = pd.DataFrame(employee_records, columns=["ID", "Name", "Salary"])

try:
    employee_data.to_csv("employees.csv", index=False)

except OSError:
    print("Unable to save employee data")

print("Employee details:")

for employee in employees.values():
    employee.display()

print(employee_data)