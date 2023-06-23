# 중복되지 않은 데이터 / 순서 없음
set1 = {}
set2 = set()

print(type(set1))
print(type(set2))

# sset1 = set([1, 2, 3, 4, 5])
sset1 = set([1, 2, 3, 4, 5, 5, 4, 3])
print(type(sset1))
print(sset1)

sset2 = {1, 2, 3, 4, 5, 5, 4, 3}
print(type(sset2))
print(sset2)

sset3 = set('hello')
print(sset3)

# print(sset1[0]) -> 순서가 없음
lsset1 = list(sset1)
print(lsset1[0])