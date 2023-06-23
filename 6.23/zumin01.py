# 입력 : xxxxxx-xxxxxxx
# 정확 / 부정확

str = input('주민번호를 입력해주세요 : ')
str = str.replace( '-', '')
print(str)

bits = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
sum = 0
for i in range(len(bits)) :
    sum += int(str[i]) * bits[i]

cnum = (11 - (sum % 11) ) % 10
lnum = int(str[-1])

if(cnum == lnum) :
    print('정확')
else :
    print('부정확')