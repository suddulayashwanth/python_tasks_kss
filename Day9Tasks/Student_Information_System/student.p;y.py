class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print()


student1 = Student("Yash", 101, 85)
student2 = Student("Madhu", 102, 90)
student3 = Student("Maddy", 103, 88)

student1.display_details()
student2.display_details()
student3.display_details()