'''
1. Advanced Default and Keyword Arguments
    ● Write a function calculate_salary that calculates the annual salary of an employee.
        ○ Thefunction should take the following arguments:
            ■ base_salary (mandatory).
            ■ bonus_percent (default is 10%).
            ■ deductions(default is 5%).
        ○ Return the calculated annual salary after applying the bonus and deductions.
    ● Call the function with different combinations of arguments, using both positional and keyword arguments.
'''

def calculate_salary(base_salary, bonus_percent=10, deduction=5):
    return base_salary + ((bonus_percent * base_salary) / 100) - ((deduction * base_salary) / 100)

# without passing default arguments
print('calculate_salary(1000000) ',calculate_salary(1000000))

# function call with all arguments
print('calculate_salary(1000000,9,3) ',calculate_salary(1000000,9,3))

# function call without passing deduction
print('calculate_salary(1000000,9) ',calculate_salary(1000000,9))

### with keyword arguments 
# we don't need to follow the order passing arguments
# function call with keyword arguments
print('\nfunction calls with keyword arguments:\n')

print('calculate_salary(deduction=2,base_salary=1000000,bonus_percent=20)',calculate_salary(deduction=2,base_salary=1000000,bonus_percent=20))

# functin call with keyword arguments without bonus
print('calculate_salary(deduction=2,base_salary=1000000)',calculate_salary(deduction=2,base_salary=1000000))

# functin call with keyword arguments without positional argument (here base salary)
# print('calculate_salary(deduction=2,bonus_percent=20)',calculate_salary(deduction=2,bonus_percent=20))
#the above call will return error

# function call with keyword arguments with only positional arguments
print('calculate_salary(base_salary=1000000)',calculate_salary(base_salary=1000000))

