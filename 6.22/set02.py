# set - 집합 : 교집합 / 합집합 / 차집합
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print(type(set1))
print(type(set2))

# 교집합
print(set1.intersection(set2))
print(set1 & set2)

# 합집합
print(set1.union(set2))
print(set1 | set2)

# 차집합
print(set1.difference(set2))
print(set1 - set2)
