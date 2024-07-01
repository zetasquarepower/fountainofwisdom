# 16.for 반복문으로 Hello, world! 100번 출력하기
for i in range(100):
    print('Hello, world')

##참고할 만한 에러 코드
# SyntaxError:invalid syntax:for반복문 형식 어긋남 :콜론 체크!!
# SyntaxError: expected an indented block: indentation 안맞음!!

for i in range(0,10,2):
    print('hello world',i)

for i in range(10,0,-1):
    print('hello world',i)
# 같은결과 as
for i in reversed(range(10)):
    print('hello world',i)

# 입력한 횟수대로 반복하기
# count=int(input())
# for i in range(count):
#     print('hello',i) input이라막음

# 시퀀스 객체로 반복하기
a=[10,20,30,40,50]
for i in a:
    print(i)

#tuple
fruits=('apples','bananas','kiwis')
for f in fruits:
    print(f)

#string
for l in 'pythonian':
    print(l, end='')
for l in reversed('pythonian'):
    print(l, end='')

#16.5 연습문제
x=[49,-17,25,102,8,62,21]

for a in x:
    print(a*10, end=' ')

#16.6 심사문제
dan=int(input())
for i in range(1,10):
    print(f'{dan} * {i} = {dan*i}')









