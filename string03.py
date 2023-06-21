#문자열 조작 : 인덱싱 / 슬라이싱
#문자열 = 문자배열

#문자열 길이
str = "Life is too short, You need Python"
print(len(str))
#n번째 글자
print(str[0])
print(str[-1]) #맨 마지막 글자

#슬라이싱 - 추출
print(str[0 : 5])
print(str[ : ])
print(str[ 10 : ])
print(str[ : 10 ])

data = '20230621흐림'
#년도, 월, 일, 날씨
year = data[0 : 4]
month = data[4 : 6]
day = data[6 : 8]
weather = data[8 : 10]
print(year, month, day, weather)

#거꾸로 집어 넣는 것은 불가
#str[0] = 'p'
#print(str)