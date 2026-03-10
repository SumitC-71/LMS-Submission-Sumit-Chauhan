'''
Task 7: File Handling with OOP
    1. Modify the Vehicle class to include a method save_to_file() that:
        ○ Savesthe details of the vehicle to a file named <brand>_<model>.txt.
    2. Write a program to:
        ○ Create a Vehicle object.
        ○ Call the save_to_file() method to save its details.
'''

class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f'info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {self.price}')

    def save_to_file(self):
        filename = f"{self.brand}_{self.model}.txt"
        with open(filename,'w') as f:
            info = f'vehicle info: \nbrand: {self.brand}\nyear: {self.year}\nmodel: {self.model}\nprice: {self.price}'
            f.write(info)
            print(f'{filename} created successfully')

car = Vehicle('Toyota','F1',2020,100000)

car.save_to_file()