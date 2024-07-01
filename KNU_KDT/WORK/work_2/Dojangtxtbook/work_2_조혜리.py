#list와 tuple
a=10
b=20
a=[38,21,53,62,19]
person=['James', 17,175.3,True]
#empty list
a=[]
b=list()

print(f'''
      {range(10)},
      {list(range(0,10))}, 
      {list(range(5,12))}, 
      {list(range(-4,10,2))},
      {list(range(10,0,-1))}''')

# tuple
a=(38,21,53,62,19)
b=38,21,53,62,19
print(id(a[0]), id(b[0]))
print(id(a), id(b)) #tuple은 같은 객체면 주소id가 같음

a=[38,21,53,62,19]
b=[38,21,53,62,19]
print(id(a[0]), id(b)) #list는 같은 객체면 주소id가 다름

a=('james',21,True,62.0,19)
b='james',21,True,62.0,19
print(id(a[0]), id(b[0]))
print(id(a), id(b)) #tuple은 같은 객체면 주소id가 같음

c=('james',)
d='james',
print(id(c),id(d)) #tuple은 같은 객체면 주소id가 같음

a=tuple(range(10))
b=tuple(range(5,12))
c=tuple(range(-4,10,2))
print(a,b,c)

a=[1,2,3]
tuple(a) # tuple ( list ) => tuple
b=(4,5,6)
list(b) # list ( tuple ) => list

a,b,c=[1,2,3]
print(a,b,c,type(a))#>> 1 2 3 <class 'int'>
d,e,f=(4,5,6)
print(d,e,f,type(d)) #>> 4 5 6 <class 'int'>

# list packing, tuple packing
a=[1,2,3]
b=(1,2,3)
c=1,2,3

# list unpacking, tuple unpacking
x=[1,2,3]
a,b,c=x

y=(4,5,6)
d,e,f=y

# x=input().split()
# a,b=x
# print(a,b) input 이라서 막음

# 10.4 연습문제, 심사문제
print(list(range(5,-10,-2)))

# data=input()
# print(tuple(range(-10,10,int(data))))  input이라서 막음

# range 덧셈 연산자로 연결할 수 없으므로 list/tuple 형변환으로 가능케할수있음
print(list(range(0,10))+list(range(10,20)))
# 곱셈 연산자도 마찬가지
print(list(range(0,10))*3)

# utf-8 문자열의 바이트 수 구하기
hello='안녕하세요'
print(len(hello.encode('utf-8')))

# .__getitem__(1)
# index 찾는 [] 이거랑 같은 거
a=[38,21,53,62,19]
print(a.__getitem__(2))

# range도 음수 인덱스로 접근 가능
r=range(0,10,2)
print(r[-3])

# 시퀀스 자료형 중에서 tuple, range, string 은 읽기 전용!

# 시퀀스 객체[:] 
print(a[:]) # a 리스트 전체
# ==
print(a[::])

# slice 객체 사용하기
print(range(10)[slice(4,7,2)]) #range(4,7,2)

a=[0,10,20,30,40,50,60,70,80,90]
s=slice(4,7)
print(a[s])
r=range(10)
print(r[s])
h='hello world'
print(h[s])
a=[0,10,20,30,40,50,60,70,80,90]

# 슬라이스에 요소 할당하기
a[2:5]=['a','b','c']
print(a)

a[2:5]=['a'] # 개수 안 맞춰도 상관없음 요소의 개수가 accordingly 줄어듬/늘어남
print(a)

a[2:5]=['a',2,2,2,6,8,45,23,1,10]
print(a)

#슬라이싱 간격을 정했을 경우
a=[0,10,20,30,40,50,60,70,80,90]
a[2:8:2]=['a','b','c']
print(a)
#>>  [0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
# 간격을 넣었을 경우 반드시 슬라이스 범위의 요소 개수와 할당할 요소 개수가 정확히! 일치해야함
# tuple, range, string은 이거 안됨!

#del
a=[0,10,20,30,40,50,60,70,80,90]
del a[2:5]
print(a) #>>      [0, 10, 50, 60, 70, 80, 90]

a=[0,10,20,30,40,50,60,70,80,90]
del a[2:8:2]
print(a) #>>      [0, 10, 30, 50, 70, 80, 90]

# 11.6 연습문제, 심사문제
# 11.6
year=[2011,2012,2013,2014,2015,2016,2017,2018]
population=[10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]

print(year[-3:], population[-3:])

#11.7
n=-32,75,97,-10,9,32,4,-15,0,76,14,2
print(n[1::2])

#11.8
# x=list(input().split()) #x=input().split()만해도 어차피 list 가 됨
# del x[-5:]
# print(tuple(x)) input이라서 막음

#11.9
a=input()
b=input()
print(a[1::2]+b[0::2])



















