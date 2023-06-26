#형변환
#bool, int, float, str
#list, tuple, dict, set

#진법변환
#bin, oct, hex

print(hex(234))
print(oct(34))

#수학관련
#abs / divmod / min / max / pow / range / round / sum

print( 7 // 3) # 몫
print(7 % 3) # 나머지
print(divmod(7, 3))

print(max('python'))
print(min('python'))

x = [10, 20, 30]
y = ['a', 'b']
for i in zip(x, y) :
    print(i)