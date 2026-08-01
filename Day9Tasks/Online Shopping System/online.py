class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty


class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, ram):
        super().__init__(name, price, warranty)
        self.ram = ram

    def display_details(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Warranty:", self.warranty)
        print("RAM:", self.ram)


phone = MobilePhone("Samsung Galaxy", 30000, "1 Year", "8 GB")
phone.display_details()