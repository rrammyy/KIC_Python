print(range(5))
print(range(0, 5))

lists = list(range(0, 5))
print(lists)

for i in range(5):
    print(i, end='\t')


sum = 0

for i in range(11):
    sum += i

print(sum)

sum1 = 0

for i in range(101):
    if i % 3 == 0:
        sum1 += i

print(sum1)