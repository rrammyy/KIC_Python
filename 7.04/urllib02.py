from urllib.parse import urlencode
from urllib.parse import parse_qs

form1 = { 'name':'glee', 'phone':'010-1111-1111'}
form2 = { 'name':'홍길동', 'phone':'010-1111-1111'}

#url - query(url 인코딩 처리)
print(urlencode(form1))
print(urlencode(form2))

print(parse_qs('name=%ED%99%8D%EA%B8%B8%EB%8F%99&phone=010-1111-1111'))