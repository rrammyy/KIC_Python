dict1 = {}
dict2 = dict()

print(type(dict1))
print(type(dict2))

# Map(Key, Value)
dict = {'name' : 'pey', 'phone' : '010-1111-1111'}
print(dict)
print(dict['name'])
print(dict.get('phone'))

dict['data1'] = 'value1'
print(dict)

dict['name'] = 'scott'
print(dict)

del  dict['data1']
print(dict)