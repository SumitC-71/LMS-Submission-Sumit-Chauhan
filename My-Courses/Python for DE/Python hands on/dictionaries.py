# mapping, dicionary
dic = {
    'name': 'sumit',
    'age': 22,
    'phone': 'samsung'
}
# d = dict(a=1, b=2)

# print(dic)
# print(dic.values())
# print(dic.keys())
# print(dic.get('name'))
# print(dic.items()) # returns list of tuples

# print(dic['nalsfdkj']) # this will return error if key not present in dictionary
# print(dic.get('aljfdk'),5) # will return 5(default value) if key present, and if not specified, it returns None, not error

# get is industrial standard

# we can create dictionary from list of tuples having 2 eles
# dic = dict([('a',1),('b',2)])
# print(dic['a'])
# print(dic.pop('a')) # this will return 1
# print(dic.pop('a',30924)) # safe of printing the feedback of poping
# print(dic['a'])

# del dic['a']
# dic.setdefault('fees',7000)
# dic2 = {
#     'fees': 5000
# }
# dic.update(dic2)
# print(dic)
# dic2 = dic.copy() # copy of dic
# dic2 = dic # reference of dic


# keys must be immutable
# you can use tuples, numeric, str as keys

