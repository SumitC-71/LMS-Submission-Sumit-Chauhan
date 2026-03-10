'''
7. Combining Lambda and Functions
    ● Write a function analyze_numbers that:
        ○ Takesalist of integers as input.
        ○ Usesmap()with a lambda function to square each number.
        ○ Usesfilter() with a lambda function to keep only numbers greater than 50
    after squaring.
        ○ Returns the filtered list.
'''

lst = [1,2,3,4,7,8,10]

def analyze_numbers(lst):
    squared = list(map(lambda x: x*x,lst))
    filtered = list(filter(lambda x: x>50,squared))
    return filtered

print(analyze_numbers(lst))