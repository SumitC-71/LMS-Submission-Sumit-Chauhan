'''
Task 6: Method Overloading
    1. Add amethod calculate_discount in the Vehicle class that:
        ○ Accepts a single argument (percentage) to calculate the discounted price.
        ○ Overloads to accept two arguments (percentage and additional discount) to
        calculate the final discounted price.
    2. Write a program to demonstrate both versions of the method.
'''


class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
    
    def display_info(self):
        print(f'brand: {self.brand}\nmodel: {self.model}\nyear: {self.year}\nprice: {self.__price}')

    def getPrice(self):
        return self.__price

    def setPrice(self,price):
        if price > 0:
            self.__price = price
        else:
            print("Price should be positive")

    def calculate_discount(self, percentage,additional_discount=0):

        price = self.__price
        discount = price * (percentage/100)
        final_price = price - discount - additional_discount

        return final_price   
    

vehicle = Vehicle("Toyota","Camry",2022,100000)

price1 = vehicle.calculate_discount(10)

price2 = vehicle.calculate_discount(10, 5000)

print("Original Price:", vehicle.getPrice())
print("Price after 10% discount:", price1)
print("Price after 10% + 5000 discount:", price2)