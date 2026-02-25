'''
2. Higher-Order Function
    ● Write a function apply_discount that:
        ○ Takestwo arguments: a price and a discount_function.
        ○ Applies the discount_function to the price and returns the discounted
    value.
    ● Define the following discount strategies as lambda functions:
        ○ Aflat discount of $50.
        ○ A20%percentage discount.
    ● Test the apply_discount function with both strategies.
'''

# Higher Order Function
def apply_discount(price, discount_function):
    return discount_function(price)

# Discount strategies as lambda functions
flat_discount = lambda x: x - 50
percent_20_discount = lambda x: x - (x * 20 / 100)

price = 500

print("Flat Discount:", apply_discount(price, flat_discount))
print("20% Discount:", apply_discount(price, percent_20_discount))