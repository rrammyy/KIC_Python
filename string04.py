#형식화된 문자열
print('I eat', 'five', 'apples')

# %뒤에 문자열이 %s로 들어감
print('I eat %s apples' % 'five')

data = 'five'
print('I eat %s apples' % data)

data1 = 'six'
data2 = 'apples'
print('I eat %s %s' % (data1, data2))

str = 'I eat %s %s' % (data1, data2)
print(str)