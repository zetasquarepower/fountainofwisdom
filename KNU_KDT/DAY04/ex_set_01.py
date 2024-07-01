#-----------------------------------------------------
# Set 자료형 살펴보기
# - 여러가지 종류의 여러개 데이터를 저장
# - 단! 중복 안됨!!!
# - 컬렉션 타입의 데이터 저장 시 Tuple 가능 (Hashable)
# - 형태 : {데이터1, 데이터1, ..., 데이터n}
#-----------------------------------------------------
## [Set 생성]-----------------------------------------
data=[]
data=()
data={}
data=set() #빈거 만들때

print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

# 여러개 데이터 저장한 set
data={10,30,20,-9,10,30,10,10} #자동으로 중복은 빠짐
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
# data의 타입: <class 'set'>, 원소/요소 개수 : 4개, 데이터 : {10, 20, 30, -9}

data={9.34, 'Apple', 10, True, '10', 10.0} #'10' 과 10은 중복값이 아님, 10과10.0은 중복값
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

#data={1,2,3,[1,2,3]} #리스트 안됨 unhashable type, 변경가능 데이터여서 안됨
data={1,2,3,(1,2,3)} # 튜플은 됨& seperate 객체랑 같아도 중복아님
data={1,2,3,(1)} # 이건 중복임
data={1,2,3,(1,)} #튜플이면 중복안됨
data={1,2,3,(1,)[0]} #이렇게 하면 또 중복됨 #>>  데이터 : {1, 2, 3}
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

# 중복제거할때 많이 쓰임

# data2={1,2,3,data}
# Error: print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
# Set은 나중에 값 바꿀 수 있음: 변경가능 따라서 안됨: Unhashable type:set

# data2={1,2,3,{1:100}} # 마찬가지로 dict도 변경가능 따라서 안됨
#>> Unhashable type:set

#그래서 collection은 Hashable type인 튜플만 가능!!

# set() 내장함수 
data={1,2,3} #=> set([1,2,3])
#=> set([1,2,3]) :대괄호의 이유는 생성자함수인 set()안에 이터러블, iterable이 들어가야하기때문
# 그래서 iterable인 string, list, tuple, dictionary 밖에 안됨 (반복가능, 데이터가 여러개있음)
data=set() # empty set
data=set({1,2,3})

# 다양한 타입 ===> set 변환
data=set([1,2,1,2,3]) # 리스트안에 중복 제거
data=set((1,2,1,2,1)) #>> {1, 2} # 튜플도 역시 중복제거
print(data)
data=set("Good")
data=set({'name':'홍길동', 'age':12,'name':'베트맨'})
print({'name':'홍길동', 'age':12,'name':'베트맨'})
print(data) #>> {'age', 'name'} key만 나옴
# 원하면 .values()나 .items() 메서드 사용

data=list('Good')
print(data)










