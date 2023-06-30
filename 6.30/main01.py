import os

print(os.path.abspath('.'))
print(os.path.abspath('..'))

#디렉토리명과 파일명 분리
print(os.path.dirname('/home/master/python2/os01.py'))
print(os.path.basename('/home/master/python2/os01.py'))

dir, file = os.path.split('/home/master/python2/os01.py')
print(dir, file)

print(os.path.join('/home/master/python2', 'os01.py'))