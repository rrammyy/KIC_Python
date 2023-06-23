print('시작')

a = 1
def func() :
    global a
    a = a + 1
    print('a1 :', a)

func()
print('a2 :', a)

print('끝')