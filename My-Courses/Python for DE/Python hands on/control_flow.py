age= 17
# one tab = 4 spaces
# space needed not to be 4(one tab) but it must be same
# like you can use 3 spaces 
if not (age < 18):
    print("above 18")
else: 
    print('below 18')

if (age < 18):
  print('not eligible for voting')
else:
  print('eligible for vote')
print('<Instruction: Must follow indentation>')

if age == 17:
    print('age == 17')

if age < 18:
    print('kiddo')
elif age <= 60:
    print('adult')
else: 
    print('senior citizen')


'''
  print('this will throw IndentationError')
the above print statement has 2 spaces and does not belong to any if or for statements
normal statements must have 0 space indentation

if (age < 18):
  print('not eligible for voting')
else:
  print('eligible for vote')

above if else has 2 space indentation (both has 2 spaces so it is valid)
'''