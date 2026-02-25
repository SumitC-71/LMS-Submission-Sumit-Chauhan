lst = range(10)
square = lambda x: x%2 == 0
evens = (filter(square, lst))
print(evens)
