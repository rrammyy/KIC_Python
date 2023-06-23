list = [1, 2, 3, 1]
print(len(list))

#
print(list.count(1))

list.append(4)
print(list)

# list.append([6, 1])
# print(list)

list.sort()
print(list)

list2 = ['a', 'd', 'c', 'b']
list2.sort()
print(list2)

# list2.reverse()
# print(list2)

print(list2.index('c'))

print(list)
list.insert(0, 4)
print(list)

list.remove(4)
print(list)

print(1 in [1, 2, 3, 4])
print(1 not in [1, 2, 3, 4])
