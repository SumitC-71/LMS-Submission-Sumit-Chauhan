'''
Task 4: Polymorphism
    1. Create another subclass Bike that inherits from the Vehicle class.
    2. Override the display_info method in the Bike class to customize its output.
    3. Write a program to demonstrate polymorphism by calling the display_info method on
    objects of Vehicle, Car, and Bike classes.

'''

class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
    
    def display_info(self):
        print(f'\nvehicle info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {self.__price}')
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self,price):
        if price > 0:
            self.__price = price
        else: 
            print('Price should be positive')

class Car(Vehicle):
    def __init__(self, brand, model, year, price, number_of_doors):
        super().__init__(brand, model, year, price)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f'\ncar info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {super().getPrice()}\nnumber of doors: {self.number_of_doors}')

class Bike(Vehicle):
    def __init__(self, brand, model, year, price, petrol_capacity):
        super().__init__(brand, model, year, price)
        self.petrol_capacity = petrol_capacity

    def display_info(self):
        print(f'\nbike info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {super().getPrice()}\npetrol capacity: {self.petrol_capacity}')

# polymorphism with 3 different objects having same method display_info
def display_info(obj):
    obj.display_info()

obj = Vehicle('Toyota','F1',2020,100000)
display_info(obj)

obj = Car('Toyota','F1',2020,100000,4)
display_info(obj)

obj = Bike('Toyota','F1',2020,100000,120)
display_info(obj)