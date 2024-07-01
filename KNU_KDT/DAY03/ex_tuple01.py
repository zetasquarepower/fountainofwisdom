# --------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
# - 다양한 종류의 여러 개 데이터를 저장하는 타입
# - List와 비슷하지만 수정, 삭제 안됨!!!!
# - 형식 : (데1,..., 데n)
#           데1,..., 데n
#          (데1,) 또는 데,
# ---------------------------------------------------------
# 튜플 데이터 생성 -----------------------------------------
datas=() #튜플만들어진거임
print(type(datas), datas, len(datas))

datas=(1,5,7)
print(type(datas), datas, len(datas))

datas=(1) #얜 그냥 int임 튜플아님
print(type(datas), datas)

datas=(1,) #쉼표있어야 튜플
print(type(datas), datas, len(datas))

datas=1 #쉼표있어야 튜플, 얜 그냥 int임
print(type(datas), datas)

datas=1, #쉼표있어야 튜플
print(type(datas), datas,len(datas))

# 튜플 데이터의 원소/요소 읽기 -----------------------------------------
datas=11,22,33,44,55
#      0  1  2  3  4
#     -5 -4 -3 -2 -1

# 2번 요소 읽기
print(datas[2], datas[-3])

# 1,2,3번 요소 일기 
print(datas[1:4])

# 요소/원소 수정 및 삭제 즉, 변경 불가!!!
datas=11,22,33,44,55
# 마지막 원소를 'A'로 변경
#datas[-1]='A' #))TypeError: 'tuple' object does not support item assignment

# 마지막 원소를 삭제해줘
#del datas[-1] #))TypeError: 'tuple' object doesn't support item deletion

# 변경하고 싶을 시에는 tuple 을 list로 형변환해주면 됨

# 튜플 데이터의 원소/요소 변경 ==> 형변환 -----------------------------------
birthday=(2024,1,1)

# 1월 ==> 3월 변경하기
birthday=list(birthday) #iterable, sequence type이라서 여기 들어갈 수 있음
birthday[1]=3
print(f'list type: {birthday}')
# list ==> tuple 형변환
birthday=tuple(birthday)
print(f'tuple type: {birthday}')









