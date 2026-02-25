'''
5. Sorting with Lambda
    ● Usethesameproducts list from Task 4.
    ● Sort the products by price in:
        ○ Ascending order.
        ○ Descending order.
    ● Print the sorted lists


    sorted function makes a sorted copy of list
'''

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Monitor", "price": 300},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600}
]

# sorted products by price in ascending order
sortedProductsAsc = sorted(products, key=lambda x: x['price'])
print(f'sorted products by price in ascending order: \n{sortedProductsAsc}')

# sorted products by price in descending order
sortedProductDesc = sorted(products, key=lambda x: -x['price'])
print(f'sorted products by price in ascending order: \n{sortedProductDesc}')

# original products list unchanged as sorted function creates copy
print(products)