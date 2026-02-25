'''
4. Using map() and filter()
    ● Create a list of dictionaries representing products in a store:
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Phone", "price": 800},
        {"name": "Tablet", "price": 600},
        {"name": "Monitor", "price": 300}
    ]
    ● Usemap()with a lambda function to calculate the price after applying a 10% discount to
    all products.
    ● Usefilter()with a lambda function to retrieve only the products with a price above
$500.
'''

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

productsAfterdiscount = list(map(lambda product: {
                           'name': product['name'],
                           'price': product['price']*0.9
                        }, products))
print('\ndiscounted products: ')
print(productsAfterdiscount)


filteredProdcuts = list(filter(lambda products: products['price'] > 500,products))
print('\nfiltered products: ')
print(filteredProdcuts)