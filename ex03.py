num1 = 10
num2 = 20
print(num1, num2)

PI = 3.14
GRAVITY = 9.8
print( PI, GRAVITY )

#참조값 중심으로 저장
print( id (num1) )
print( id (num2) )

#값이 아닌 참조값을 넘김
num3 = num1
print( id (num1) )
print( id (num3) )