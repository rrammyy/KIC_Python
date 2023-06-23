print('시작')

def func1() :
    pass
def func2() :
    print('함수 호출')
def func3(a) :
    print('함수 호출 : ', a)
def func4(a) :
    print('함수 호출 : ', a)
    return a


func1()
func2()
func3(10)

print(func4(20))
print('끝')