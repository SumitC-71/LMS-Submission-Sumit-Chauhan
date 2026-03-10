'''
python supports all paradiam of programming:

functional programming:
small modules/functions that does not change the state

procedure programming: 
small modules/functions that modifies the state

object oriented programming:
attributes and method
[ the way you think to code with real life solutions ]

class - design/blueprint
object - instance

everything in python is object: 9, 'sumit', [] etc.

# <class '__main__.Computer'>
# here module name is main, and class is Computer

special variable: __name__
special method: __init__

everything stores in heap in python

# checking the address of object in heap
print(id(comp1))

size of an object depends on type and no of objects

types: instance variable, class(static) variable
variables declared inside __init__ are instance variable
variables declared outside __init__ are class(static) variable

namespace is an area where you create and store objects/variables

instance namespace & static namespace

getters and setters

instance methods: accessors (which just accesses the value) and mutators (which change the value)

instance method: self which accesses instance variables
class method: cls which accesses class variables
static method: noting to add, this is used for common use and does not accessing class or instance variables 

concept of inner classes: 
there is a student class and it has some attributes 
some of those attributes are specification of his laptop
now when you create __init__  or other method, you need to pass all the specifications of laptop as parameters
instead of which you can create a laptop class inside student

class Student:
    def __init__(self,laptop:
        
    class Laptop:


'''

'''
class Computer:
    name='DELL'


    def __init__(self,cpu,ram): # contructor or the method that calls itself
        self.cpu=cpu
        self.ram=ram
        print('in init')

    def config(self):
        print(f'{self.cpu}, {self.ram}, 256GB')

    def compare(self,other):
        if self.ram > other.ram:
            return True
        return False

    @classmethod   # for tellign this is class method and not instance
    def info(cls):
        return cls.name

comp1 = Computer('i5',16)
print(type(comp1))

comp2 = Computer('i6',16)
print(id(comp1.ram))
print(id(comp2.ram))


comp1.config()  # behind the scene everything as the line below
# Computer.config(comp1)
'''


'''
Inheritencd:
# simple inhertitance
class A:

class B(A):

# multilevel
class C(B):



# multiple
class A:
class B:
class C(A,B):

contructors in in hertitance:
if you b inherites a,
and you create an object of b then first compiler will check for contructor of b if not found then only it will go for a's contructor

'''

class a:
    def __init__(self):
        print('init a')
    
    def feature(self):
        print('feature A')
        
class b:
    def __init__(self):
        super().__init__() # this method will call contructor of a
        print('init b')
    
def feature(self):
        print('feature b')

# bb=  b()

# in-case of multiple inheritance
class c(a,b):
    def __int__(self):
        super().__init__()  # here MRO (method resolution ordre ) comes into picture
        # it checks for left right 
        print('init c')
        
cc = c()
cc.feature()
    
# if a and b both have same method, MRO will choose the one which comes first in C(a,b) which a in this case

'''
loose coupling
dependency injection
interface
'''


'''
Polymorphism:

> duck typing
> operator overloading
> method overloading
> method overridding
'''


'''
duck typing:
dynamic typing

x = 5
x = 'sumit'

object created of 5 or 'sumit'
x is just a name for it

class CSVLoader:
    def load(self):
        print("Loading CSV file")

class JSONLoader:
    def load(self):
        print("Loading JSON file")

class DatabaseLoader:
    def load(self):
        print("Loading from database")

def process_data(loader):
    loader.load()

process_data(CSVLoader())
process_data(JSONLoader())
process_data(DatabaseLoader())




'''

a=5
b=2
print(a+b)
print(int.__add__(a,b)) # we call it a magic method


'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overload + operator
    def __add__(self, other):
        return self.marks + other.marks

    # Overload > operator
    def __gt__(self, other):
        return self.marks > other.marks

    # String representation
    def __str__(self):
        return f"Student(Name: {self.name}, Marks: {self.marks})"


s1 = Student("Aakash", 85)
s2 = Student("Rahul", 78)

print(s1)  # Uses __str__

print("Total Marks:", s1 + s2)

if s1 > s2:
    print(f"{s1.name} has more marks")
else:
    print(f"{s2.name} has more marks")


'''



'''
Method Overloading (Python way – using default arguments)
class Calculator:

    def add(self, a, b, c=0):   # default argument handles overloading
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))        # 2 arguments
print(calc.add(10, 20, 30))    # 3 arguments
'''

'''
Method Overriding  -> runtime polymorphism
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):   # overriding parent method
        print("This is Child class")


obj = Child()
obj.show()

'''


class a:
    def __init__(self):
        self.__salary=1000
    
class b(a):
    def show(self):
        print(bb._a__salary)

bb = b()
bb.show()


# class Parent:
#     def __init__(self):
#         self.__salary = 50000

# class Child(Parent):
#     def show(self):
#         print(obj._Parent__salary)

# obj = Child()
# obj.show()