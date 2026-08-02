def add_bonus(function):
    def wrapper(employee):
        bonus = employee.salary * 0.10
        employee.salary += bonus

        print("Bonus Added:", bonus)
        function(employee)

    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary After Bonus:", self.salary)


employee1 = Employee("Yash", 50000)
employee1.display_salary()