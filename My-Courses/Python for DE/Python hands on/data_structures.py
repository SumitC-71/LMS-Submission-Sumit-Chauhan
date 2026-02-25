print("hello world")

# None 


# data type: numeric
num = 2.5
print("flt type: ",type(num))

num = 2
print("flt type: ",type(num))

num = 2 + 5j
print("flt type: ",type(num))

num = True
print("flt type: ",type(num))

# type conversion
num = 3.4
numInt = int(num)
print("numInt: ", numInt)

num = float(numInt)
print("numInt::float ", num)

real,imag=4,5
c = complex(real,imag)
print(c)

print("real < imag: ", real < imag)

# True is 1, False is 0  >> True not true!!

# sequences 
lst = [1,2,3,4,5]
print(type(lst))
lst.append(6)
print(lst)

st = {1,2,3,4,5}
print(type(st))

tpl = (1,2,3)
print(type(tpl))

string = "str"   
print(type(string))  # class name: str

rng = range(10)  # start: 0, 10 excluded
print(rng)
print(list(rng))

# range parameters: (start, end, jump)
print(list(range(2,11,2)))  


