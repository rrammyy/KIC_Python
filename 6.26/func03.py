#help(all)

#all - 순회할 수 있는 요소 전체 참이면 참
print(all([]))
print(all([True, True]))
print(all([True, False]))

print(all([0]))
print(all([0, 1, 2, 3]))
print(all([1, 2, 3]))

#any - 순회할 수 있는 요소 하나가 참이면 참
print(any([]))

#ascii code 변환
print(chr(97))
print(chr(48))
print(ord('a'))
print(ord('0'))

#list
for name in ['body', 'food', 'bar'] :
    print(name)

for i, name in enumerate(['body', 'food', 'bar']):
    print(i, name)

print('1+2')
print(eval('1+2'))