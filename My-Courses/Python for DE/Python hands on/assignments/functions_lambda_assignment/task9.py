'''
9. Data Transformation
    ● Giventhe following data:
    data = [
        {"name": "Alice", "age": 30, "score": 85},
        {"name": "Bob", "age": 25, "score": 90},
        {"name": "Charlie", "age": 35, "score": 95}
    ]
    ● Useacombination of map() and lambda functions to:
        ○ Extract the names of all individuals.
        ○ Calculate the average score of all individuals.
'''
from functools import reduce

data = [
        {"name": "Alice", "age": 30, "score": 85},
        {"name": "Bob", "age": 25, "score": 90},
        {"name": "Charlie", "age": 35, "score": 95}
]

# extracted names
names = list(map(lambda person: person.get('name'),data))
print(names)

# average score
total_score = sum(map(lambda person: person["score"], data))
average_score = total_score / len(data)

print(average_score)
