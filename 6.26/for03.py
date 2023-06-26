lists = [1, 2, 3, 4]
#각 값에 * 3
#result = []
#for list in lists :
#    result.append(list * 3 )

#print(result)

result = [list * 3 for list in lists]
print(result)

results = [[list + 10, list * 10] for list in lists]
print(results)

lists1 = [2, 3]
lists2 = [4, 5]

result = [list1 * list2 
          for list1 in lists1 
          for list2 in lists2]
print(lists1)
print(lists2)
print(result)
