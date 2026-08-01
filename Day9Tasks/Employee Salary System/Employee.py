class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def display_details(self):
        print("Manager Name:", self.name)
        print("Salary:", self.salary)


manager1 = Manager("Ramesh", 60000)
manager1.display_details()