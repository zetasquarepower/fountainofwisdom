# --------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
# - 내장함수 : len(), max(), min(), sum()
# - 연산자 :덧셈, 곱셈, 멤버연산자 
# ---------------------------------------------------------
nums=11,22,33,44,55

## 내장함수 ------------------------------------------------
print(f'nums 개수 : {len(nums)}개')
print(f'최대값 : {max(nums)}개 최소값 : {min(nums)}')
print(f'합계: {sum(nums)}')
print(f'정렬: {sorted(nums)}') #sorted(n)=> Ascending order
print(f'정렬: {sorted(nums,reverse=True)}') #sorted(n,reverse=True) => Descending order
# sorted(): iterable 데이터 타입만 가능
# sum(): 문자열/str 안됨!!

print(max('abc','abC')) #이건 됨
print(sorted(['abc','Zoo']))
#print(sum(['abc','Zoo'])) # sum(): 문자열/str 안됨!!

## 연산자 --------------------------------------------------
## 덧셈
data1=11,22
data2='A','B','C'
data3=[1,2]
print(data1+data2) # tuple + tuple = tuple
# =>(11, 22, 'A', 'B', 'C') 두개의 튜플을 더하면 한개의 튜플로 만듬

#print(data1+data3) # tuple + list = ERROR 안됨!
# 따라서 덧셈하고싶으면 형변환 해야함
print(data1+tuple(data3))


# 곱셈 : tuple*int (tuple*tuple은 안됨!)
print(data1*3) 
# 리스트도 같음

## 멤버 연산자 => in, not in 
print(11 in data1) #True
print('A' in data1) #False

##iterable data type 3개: list, tuple, string
















