class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area of rectangle:", area)


rectangle1 = Rectangle(10, 5)
rectangle1.calculate_area()