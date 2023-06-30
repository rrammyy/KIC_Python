import os

#print(os.listdir('.'))

for list in os.listdir('.') :
    print( os.path.isdir(list), ':', list )