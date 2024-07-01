# ------------------------------------------------------------
# 내장함수 map(함수명, 여러개데이터) 
# ------------------------------------------------------------
data=input('숫자데이터 입력 : ')

print(type(data), data)

# 1개 문자열 ==> 여러개 문자열 분리
# 예) '10 20 30' ===> '10', '20', '30'
nums=data.split()
a,b,c=map(int,data.split())
print(a, id(a))

# 문자열 숫자 ==> 정수로 형변환
result=map(int,nums)
print(type(result), result)

myfunc=int # 같은 주소id을 갖고있음 
result2=map(myfunc,nums)
print(id(int),type(result2), result)
