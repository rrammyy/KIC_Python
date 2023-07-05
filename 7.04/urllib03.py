from urllib.request import urlopen

urldata = urlopen('https://www.daum.net')
#print(urldata)

#print(urldata.header)

html = urldata.read()
enchtml = html.decode('utf-8')
print(type(enchtml))