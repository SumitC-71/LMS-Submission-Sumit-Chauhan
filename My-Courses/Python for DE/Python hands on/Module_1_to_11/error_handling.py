'''
types  of error: 
    logical error
    compilation error
    runtime error

Exception as e 
here e is Exception object

ZeroDivisionError
ValueError

'''

# a = 2
# b = 0

# try:
#     print(a/b)
# except Exception as e:
#     # print('Error: you cannot divide a number by zero')
#     print(f'Error: {e}')

# print('bye')

# e here is Exception object

# you can uses multiple except blogs

# finally block will execute even if there is an error or not
# we use it to close all the resources that are opened in or before try block

# else block will execute only if there is no error (for showing success message)

'''
try:
    print('Resource opened')
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e)
else:
    print('success!!')
finally: 
    print('Resource closed')
'''

# raising custom error
# def withdrawal(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     return balance - amount
    

# try:
#     print('transaction starts')
#     balance = 1000
#     amount = int(input('Enter the amount you want to withdraw: '))
#     balance = withdrawal(balance=balance, amount=amount)
#     print(f'remaining balance: {balance}')

# except Exception as e:
#     print(e)
# else:
#     print('Amount withdrawal successfully')

# finally:
#     print('transaction closed')


'''
commont exception types: 

| Exception         | When It Happens         |
| ----------------- | ----------------------- |
| ValueError        | Wrong value type        |
| TypeError         | Wrong data type         |
| KeyError          | Dictionary key missing  |
| IndexError        | List index out of range |
| FileNotFoundError | File missing            |
| ZeroDivisionError | Divide by 0             |
| ImportError       | Module not found        |
| AttributeError    | Wrong object attribute  |



resources that should be closed: 
    Close DB connections
    Close files
    Release memory



'''

# retry pattern
import time

for i in range(3):
    try:
        num = int(input('Enter the number: '))
        result = 10 / num
        print(f'Successfull division, result: {result}')
        break
    except ZeroDivisionError:
        print('cannot divide by zero')
        print("Retrying...")
        time.sleep(1)
    except TypeError:
        print('Invalid input')
        print("Retrying...")
        time.sleep(1)
    except Exception as e:
        print(f'Something went wrong: {e}')
        print("Retrying...")
        time.sleep(1)

# TODO: assert, logging with error handling
