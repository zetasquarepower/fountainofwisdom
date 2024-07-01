# -------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수 
# ---------------------------------------------------

person={'name':'홍길동', 'age':20,  'job':'학생'}
dog={'breed':'골든리트리버', 'weight': '35kg', 'color':'golden', 'gender':'male','age':5}
jumsu={'국어':90, '수학':178, '체육':100}

## [연산자]-----------------------------------------
# 산술 연산 (덧셈 등) 안됨! X
# person+dog error

# 멤버 연산자 : in, not in
#    key
print('name' in dog) # False
print('name' in person) # True

#    value : dict 타입에서는 key만 멤버연산자로 확인
print('골든리트리버' in dog) # 키가 아닌 값으로 해서 False
print(20 in person) # 키가 아닌 값으로 해서 False

# value 추출 ==> method 인 .values()써라
print('골든리트리버' in dog.values()) # True
print(20 in person.values()) # True

## [내장함수]------------------------------------------------
## - 원소/요소 개수 확인 : len()
print(f' dog의 요소 개수 : {len(dog)}개')
print(f' person의 요소 개수 : {len(person)}개')

## - 원소/요소 정렬 : sorted() ==> 키만 나옴
# - 키 만 정렬, 값은 안나옴
print(f' dog key 오름차순 정렬 : {sorted(dog)}')
print(f' dog key 내림차순정렬 : {sorted(dog, reverse=True)}')

# - 값만 정렬
#Error: print(f' dog 값 정렬 : {sorted(dog.values())}') # 타입이 섞여있어서 안됨
print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.values())}') #안에 타입이 일치할 경우 괜찮음
print(f' jumsu key 오름차순 정렬 : {sorted(jumsu)}')

# jumsu 값 오름차순 정렬 : [90, 100, 178]
# jumsu 값 오름차순 정렬 : ['국어', '수학', '체육'] ==>키값만 오름차순, not jumsu

print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.items())}')
# jumsu 값 오름차순 정렬 : [('국어', 90), ('수학', 178), ('체육', 100)]
# 키으로 정렬됨 우리는 값으로 했으면하는데..
# 그래서 이걸 씀!!

#*************************************************************************
print(f' jumsu 값 오름차순 정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')
# 원래 x에서의 1번인덱스 값으로 정렬하고싶을때 
#*************************************************************************

# - 동일한 타입에서 정렬 가능함 --------------------------------------------------
n1=[1,4,9,-2]
n2=['a','F','Z']
n3=[1,'A',4,-8,'hehe']
print(sorted(n1), sorted(n2)) # 값의 타입이 통일되면 정렬 문제없음
#print(sorted(n3)) 이거는 안에 타입이 달라서 정렬 안됨!































