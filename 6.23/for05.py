name = input('이름을 입력해주세요 : ')
print(name)

names = name.split(' ')

for i in range(len(names)) :
#    print(names[i])
    names[i] = names [i][0].upper() + names[i][1:]
    #print(names[i])

result = ' '.join(names)
print('결과 : ', result)

#for data in names :
#    print(data)