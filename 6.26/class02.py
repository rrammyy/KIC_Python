class Cookie :
    #클래스 멤버 변수
    a = 10

c1 = Cookie()
#print(c1.a)
print(Cookie.a)

c2 = Cookie()
#c2.a = 20 (X) - 인스턴스 멤버로 쓰임
#클래스 멤버 변수
Cookie.a = 20
#print(c2.a)
#print(c1.a)
print(Cookie.a)

print(id(c1.a))
print(id(c2.a))