'''
nums = [1000,3,4,5,4,4,4,2000]

print(nums.__iter__())  # iter method returns the whole object

it = nums.__iter__()


try:
    print(it.__next__()) # method returns the current value and jumps to next item
    print(it.__next__())

    print(next(it))      # this also works

    for i in nums:       # this will iterate from start
        print(i)

    print(next(it))

except StopIteration as sI:
    print(f'Iteration completed')


class TopTen:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self

    def __next__(self):   # automatically next(inc) works 
        val = self.num
        if val > 10:
            raise StopIteration
        self.num += 1
        return val
    
inc = TopTen()
print(next(inc))
print(next(inc))
print(inc.__next__())

for i in iter(inc):  # iter(inc) or inc both will work
    print(i)
# this loop will continue from 4 (where it was paused) and will stop on StopIteration exception automatically

'''
 

########################################
#           Generator
########################################


def top_ten():
    num = 1
    while num <= 10:
        yield num
        num += 1

it = top_ten()

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for i in it:
    print(i)
  