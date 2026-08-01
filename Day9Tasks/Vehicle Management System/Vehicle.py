class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Car(Vehicle):
    def display_details(self):
        print("Car Brand:", self.brand)
        print("Car Speed:", self.speed, "km/h")


class Bike(Vehicle):
    def display_details(self):
        print("Bike Brand:", self.brand)
        print("Bike Speed:", self.speed, "km/h")


car1 = Car("Toyota", 180)
bike1 = Bike("Yamaha", 120)

car1.display_details()
print()
bike1.display_details()