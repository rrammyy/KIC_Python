str = 'a:b:c:d'
list = str.split(':')
print(type(list))

print(list)

str2 = '.'.join(list)
print(str2)

print(':'.join('abcd'))