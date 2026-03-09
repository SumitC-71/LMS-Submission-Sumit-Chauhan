'''
Task 1: Create a Class
    1. Create a class named Vehicle with the following attributes:
        ○ brand(string)
        ○ model(string)
        ○ year(integer)
        ○ price(float)
    2. Add amethod display_info that prints all the details of the vehicle.
    3. Create an object of the Vehicle class and call the display_info method.

'''

class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f'info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {self.price}')
    
car = Vehicle('Toyota','F1',2020,100000)
car.display_info()




