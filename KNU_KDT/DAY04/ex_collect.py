# ------------------------------------------------------------------
# Collection 자료형에 공통적인 부분 살펴보기 
# ------------------------------------------------------------------
## [여러개의 변수에 데이터 저장 ]-------------------------------------
# name='홍길동'
# age=12
# job='의적'
# gender='남'
# 팩킹(packing) 방식 : 변수명=tuple 타입
data='홍길동', 12, '의적', '남'

#--------------------------------------------------------------------
# 언패킹(unpacking) 방식 :변1, 변2,..., 변n = tuple 타입
#                        변수명 개수 == 데이터 수 [필수!]
#--------------------------------------------------------------------
name, age, job, gender ='홍길동', 12, '의적', '남' #우변은 소괄호 없는 튜플
print(name, age, job, gender)
#name, age ='홍길동', 12, '의적', '남' #Error =>숫자일치해야되서 이건 안됨

name, age, _, _ ='마징가', 10, '의적', '남' 
#필요없는 데 이거 써야할때 그냥 placeholder로 _가 쓰임
print(name, age,_) #_뒤에꺼가 쓰임 _ :의미없는 데이터의 변수명 ''따옴표안써도됨


jumsu=[100,99]
kor,math=[100,99] # list 로도 언패킹 가능
kor, math=jumsu # 이거도 됨
print(jumsu, kor, math) #>>  [100, 99] 100 99

person={'name':'박', 'age':11}
k1,k2={'name':'박', 'age':11} # dictionary 로도 언패킹 가능
print(person, k1,k2) #>>  {'name': '박', 'age': 11} name age #뒤에는 key만 나옴
k1, k2=person # 이거도 됨 위코드와 똑같은 결과
print(person, k1,k2) #>>  {'name': '박', 'age': 11} name age #뒤에는 key만 나옴

#--------------------------------------------------------------------
# 생성자(Constructor) 함수: 타입명과 동일한 이름의 함수
# - int(), float(), str(), bool(), list(), tuple(), dict(), set()
# - map(), range() 
#--------------------------------------------------------------------
# 기본 데이터 타입 
num=int(10)      # num=10
fnum=float(10.2) # fnum=10.2
msg=str('Good')  # msg='Good'
isOk=bool(False) # isOk=False
#or 0 or empty
print(num, fnum, msg, isOk)

#컬렉션 데이터 타입
lnums=list([1,2,3,4])  # lnums=[1,2,3,4]
tnums=tuple((3,6,9))   # tnums=(3,6,9)
ds=dict(d1=10, d2=30) #아니면
ds=dict({'d1':10, 'd2':30}) # ds={'d1':10, 'd2':30}
ss=set({1,1,3,3,5}) #ss={1,1,3,3,5}
print(lnums, tnums, ds,ss)

#타입 변경 => 형변환 ------------------------------------------------------------
# dict 자료형은 다른 자료형과 달리 데이터 형태가 다름
# - 데이터 형태 => 키:값
# - dict(키1=값, 키2=값,...) 이런 형태로 들어가야함 :키는 str만 가능, '' or "" 사용불가!
ds=dict(n1=1, n2=2, n3=3) #키=>문자열일때 홑따옴표 안함 여기 키는 숫자도 안됨:변수명같이 취급
ds=dict(name=1, age=2, gender='남') # 데이터값만 str처리
print(ds)

ds=dict([('name','마징가'),('age',12)]) # 리스트안에 원소가 튜플/리스트면 됨 키,값 같이 주면 됨
print(ds)

ds=dict([['name','마징가'],['age',12]]) # 리스트안에 원소가 리스트여도 same
print(ds)

h1=['name','마징가']
h2=['age',12]
ds=dict([h1,h2]) # 이것도 됨
print(ds)

# ds=dict([['name','age','gender'],['마징가',12,'남']])
# print(ds) ERROR

##내장함수 :zip():같은 인덱스의 요소끼리 묶어줌 (튜플도 됨 iterable 됨)
l1=['name','age','gender']
l2=['마징가',12,'남']
print(list(zip(l1,l2)))

l1=['name','age','gender']
l2=['마징가',12,'남']
l3=[False,True,True]
print(list(zip(l1,l2,l3))) # 이것도 다 묶어버림
#>> [('name', '마징가', False), ('age', 12, True), ('gender', '남', True)]

ds=dict(zip(l1,l2))
print(ds)








