#3.7 연습문제, 심사문제
print('Hello, world!')
print('Python Programming')
print('Hello, world!','Hello, world!', sep='\n')
a=10
if a == 10:
    print('10입니다')

if a == 10:
    print('10')
    print('입니다')

d=divmod(5,2)
print(f'divmod(5,2) = {d}')
# 튜플 형태
quotient, remainder=divmod(5,2)
print(quotient, remainder)
print(f'''
{float(1+2)}
{float("5.3")}
{1.2+1.3j}
{complex(1.2,1.3)}
{10/4}''')

#5.5 연습문제, 심사문제
print(int(0.2467*12+4.159))
print(102*0.6+225)

#6--------------------------------
print(f'''
      {type('Hello')}
      
      ''')
x,y,z=1,2,3
print(x,y,z)
x=y=z=9
print(x)
x,y=1,5
x,y=y,x
print(x,y)
# 변수 삭제하기
x=10
del x
# print(x)

#빈변수만들기
x=None
print(x) # returns 'None'
#변수계산
a=10
b=20
c=a+b
print(c)

a=10
a=a+20
print(a) #30
a=10
a+=20 #************************새로운방식!*****************
print(a)
a=10
print(f'a += 20 == a=a+20 == a={a+20}')
a=10
print(f'a -= 20 == a=a-20 == a={a-20}')
a=10
print(f'a *= 20 == a=a*20 == a={a*20}')
a=10
print(f'a /= 20 == a=a/20 == a={a/20}')
a=10
print(f'a //= 20 == a=a//20 == a={a//20}')
a=10
print(f'a %= 20 == a=a%20 == a={a%20}')

#부호붙이기
x=-10
print(-x)

#두 숫자의 합 구하기
a=input('첫번째 숫자를 입력하세요:')
b=input('두번째 숫자를 입력하세요:')
print(a+b) #str 이므로 산수안됨

a=int(input('첫번째 숫자를 입력하세요:'))
b=int(input('두번째 숫자를 입력하세요:'))
print(a+b) #int 형변환으로 이제 산수됨


















