'''
title: Student Performance & Access Management System 
domain: edTech
task: simulation of real-world Trainee evaluation workflow

'''

###  1. Login Validation 
users = { 
    "trainer1": "Train@123", 
    "trainer2": "Learn@123" 
}

# login_attempts = 3
# in this exercise, control flow usage is emphasize so we are using nested loops
# otherwise we can use loops for better code
loggedIn = False

# attempt 1
name = str(input("Pleaes Enter your name: "))
password = str(input("Pleaes Enter your password: "))
if users.get(name) == password:
    loggedIn = True
else:
    print('invalid Credentials!')
    # attempt 2
    name = str(input("Pleaes Enter your name: "))
    password = str(input("Pleaes Enter your password: "))
    if users.get(name) == password:
        loggedIn = True
    else:
        print('invalid Credentials!')
        # attempt 3
        name = str(input("Pleaes Enter your name: "))
        password = str(input("Pleaes Enter your password: "))
        if users.get(name) == password:
            loggedIn = True
        else:
            print('invalid Credentials!')

print('\n')
if loggedIn:
    print('Welcome, ',name)
else:
    print('Access Denied. Please contact admin.')

### 2. Trainee Data Entry

trainees = []
while True:
    name = str(input("Enter trainee name: "))

    python_marks = int(input("Enter python marks: "))
    while not (python_marks >= 0 and python_marks <= 100):
        print('invalid marks')
        python_marks = int(input("Enter python marks: "))

    data_structures_marks = int(input("Enter data structure marks: "))
    while not (data_structures_marks >= 0 and data_structures_marks <= 100):
        print('invalid marks')
        data_structures_marks = int(input("Enter data structure marks: "))

    control_flow_marks = int(input("Enter control-flow marks: "))
    while not (control_flow_marks >= 0 and control_flow_marks <= 100):
        print('invalid marks')
        control_flow_marks = int(input("Enter control-flow marks: "))
    
    trainee = {'name':name, 'python_marks':python_marks, 'data_structures_marks':data_structures_marks, 'control_flow_marks':control_flow_marks }
    trainees.append(trainee)

    ex = int(input("Enter 0 for exit\n1 for continue adding student info\n"))
    if not ex:
        print('breaking the loop')
        break
    
print("trainees information: ")
print(trainees)
### 3. Performance Evaluation
print('\nPerformance Evaluation')

for trainee in trainees:
    total_marks = trainee.get('python_marks') + trainee.get('data_structures_marks') + trainee.get('control_flow_marks') 
    avg_marks = total_marks/3
    print('\nname: ', trainee.get('name'))
    print(f'total marks: {total_marks}')
    print(f'average marks: {avg_marks}')

    trainee['total_marks'] = total_marks
    trainee['average_marks'] = avg_marks

    if avg_marks >= 85:
        trainee['grade'] = 'Excellent'
    elif avg_marks >= 70:
        trainee['grade'] = 'Good'
    elif avg_marks >= 50:
        trainee['grade'] = 'Average'
    else:
        trainee['grade'] = 'needs improvement'
    
    print(f'feedback: {trainee['grade']}')

### 4. Analytics & Reporting 
print('\n')
highest_scorer = None
highest_marks = 0
lowest_scorer = None
lowest_marks = 101
for trainee in trainees:
    if trainee['average_marks'] > highest_marks:
        highest_marks = trainee['average_marks']
        highest_scorer = trainee['name']
    if trainee['average_marks'] < lowest_marks:
        lowest_marks = trainee['average_marks']
        lowest_scorer = trainee['name']

print(f'highest scorer: {highest_scorer} with {highest_marks} average marks')
print(f'lowest scorer: {lowest_scorer} with {lowest_marks} average marks')

grades = {'Excellent':0, 'Good':0, 'Average':0, 'needs improvement':0}
for trainee in trainees:
    grades[trainee['grade']] += 1

for grade,count in grades.items():
    print(f'total of {count} students got {grade} grade')

failed_students=[]
for trainee in trainees:
    failed = False
    if trainee['python_marks'] < 40:
        failed = True
    if trainee['data_structures_marks'] < 40:
        failed = True
    if trainee['control_flow_marks'] < 40:
        failed = True

    if failed == True:
        failed_students.append(trainee['name'])

print(f'failed student list: {failed_students}')


### 5. Trainer Decision Module
print('\n')
remedial_flag = str(input("Do you want to schedule remedial training? (yes/no)"))

if remedial_flag == 'yes':
    print(f'list of students who need remedial training: {failed_students}')
elif remedial_flag == 'no':
    print('Report finalized successfully')
else:
    print('you have entered invalid option')

