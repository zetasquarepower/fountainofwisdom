# -------------------------------------------------
# Dict 자료형 살펴보기
# - Dict 자료형 전용의 함수 즉, 메서드(Method) 사용
# - 사용법 : 변수명.메서드명()
# ---------------------------------------------------
## [Dict에서 key만 추출하는 메서드 .keys()  ]---------------------------------

p1={'name':'홍길동', 'age':20,  'job':'학생'}

# dict_keys[] ==> view 타입임
result=p1.keys()
print(f'key 추출 : {result}, {type(result)}')
# Error : print(result[0])

# 원한다면 list 로 형변환 => list( dict_keys타입 )
result=list(result)
print(f'key 추출 : {result}, {type(result)}')

## [Dict에서 값/데이터 만 추출하는 메서드 .values()  ]---------------------------------
result=p1.values()
print(f'값 추출 : {result}, {type(result)}') #==> returns class 'dict_values'

## [Dict에서 값/데이터 만 추출하는 메서드 .items()  ]---------------------------------
result=p1.items()
print(f'키와 값 묶음 추출 : {result}, {type(result)}') #==> 튜플인 dict_items 로 return

result=list(result)
print(f'키와 값 묶음 추출 : {result[0]}, {type(result[0])}') #==>튜플로 반환





















