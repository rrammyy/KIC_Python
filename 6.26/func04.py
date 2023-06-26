lists = [1, -3, 2, 0, -5, -6]

#양수만을 필터링 후 출력하는 함수 제작
def positive1(lists) :
    result = []
    for i in lists :
        if i > 0 :
            result.append(i)
    return result

def positive2(x) :
    return x > 0

print(positive1(lists))

result = list(filter(positive2, lists))
print(result)