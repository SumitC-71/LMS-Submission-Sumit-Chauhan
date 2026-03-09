'''
Task 2: Encapsulation
    1. Modify the Vehicle class:
        ○ Makethepriceattribute private.
        ○ Addgetter and setter methods for price to access and modify it.
    2. Write a program to:
        ○ Create a Vehicle object.
        ○ Usethesetter method to set the price.
        ○ Usethegetter method to retrieve and display the price.
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
    
car = Vehicle('Toyota','F1',2020,100000)
car.display_info()

car.setPrice(200000)
print(f'Price of car: {car.getPrice()}')