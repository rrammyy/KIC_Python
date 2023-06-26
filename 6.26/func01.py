def outerfunc() :
    data = 1
    #지역
    def innerfunc() :
        print('내부함수 호출')
        
        nonlocal data
        print(data)
        data = 2
        print(data)
        
    innerfunc()
    print(data)
    
outerfunc()