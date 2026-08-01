class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id


class Professor(Staff):
    def display_details(self):
        print("Professor:", self.name)
        print("Staff ID:", self.staff_id)


class LabAssistant(Staff):
    def display_details(self):
        print("Lab Assistant:", self.name)
        print("Staff ID:", self.staff_id)


class Administrator(Staff):
    def display_details(self):
        print("Administrator:", self.name)
        print("Staff ID:", self.staff_id)


professor = Professor("Dr. Kumar", 101)
assistant = LabAssistant("Ravi", 102)
administrator = Administrator("Anitha", 103)

professor.display_details()
print()
assistant.display_details()
print()
administrator.display_details()