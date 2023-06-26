class Cookie :
    #def func1() :
    #    print('func1 호출')
    a = 20

    def func1(self) :
        print('func1 호출')
        # self = 자바의 this
        print(self)

    def func2(self, a) :
        print(a)
        #인스턴스 멤버변수 선언
        self.a = a
    
c1 = Cookie()
c1.func1()
c1.func2(10)
print(c1.a)
print(Cookie.a)