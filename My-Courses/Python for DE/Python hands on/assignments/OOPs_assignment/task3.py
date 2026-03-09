'''
Task 3: Inheritance
    1. Create a subclass Car that inherits from the Vehicle class.
    2. Add an additional attribute to the Car class:
        ○ number_of_doors (integer)
    3. Override the display_info method in the Car class to include the number of doors.
    4. Create an object of the Car class and call the display_info method.

'''

class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
    
    def display_info(self):
        print(f'info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {self.__price}')
    
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
        print(f'info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {super().getPrice()}\nnumber of doors: {self.number_of_doors}')

car = Car('Toyota','F1',2020,100000,4)
car.display_info()
