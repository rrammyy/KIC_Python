data = 10
print(data)

# 다중 할당
data1, data2 = (10, 20)
print(data1, data2)

(data1, data2) = 10, 20
print(data1, data2)

data1, data2 = 10, 20
print(data1, data2)

# 변수 값의 할당
a = 3
b = 5
a, b = b, a
print(a, b)

# 변수 값의 교환
a = 3
b = 5
c = 7
a, b, c = c, a, b
print(a, b, c)

[a, b] = [10, 20]
print(a, b)