def add_attr(cls):
    cls.country = "India"
    print('Decorator add_attr')
    return cls

@add_attr
class Person:
    def __init__(self):
        print('Person created')
    pass

p = Person()
print(p.country)