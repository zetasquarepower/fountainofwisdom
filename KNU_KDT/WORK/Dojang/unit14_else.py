# 14. else를 사용하여 두 방향으로 분기하기
x=5
if x==10:
    y=x
else:
    y=0
print(y)

x=5
y= x if x==10 else 0
print(y)
print('*'*30)

# if 조건문 동작 방식
if True:
    print('참')
else:
    print('거짓')
print('*'*30)
if False:
    print('참')
else:
    print('거짓')
print('*'*30)
if None: #None은 False
    print('참')
else: print('거짓')

#if 조건문에 숫자 지정하기
if 0: # 0:False
    print('참')
else:
    print('거짓')
print('*'*30)

if 1: #1:True
    print('참')
else:
    print('거짓')
print('*'*30)

if 0x1F: #:True
    print('참')
else:
    print('거짓')
print('*'*30)

if 0b1000: #:True
    print('참')
else:
    print('거짓')
print('*'*30)

if 13.5: #:True
    print('참')
else:
    print('거짓')

# if에 문자열 지정
if 'Hello': #:True
    print('참')
else:
    print('거짓')
print('*'*30)

if '': #empty str: False
    print('참')
else:
    print('거짓')
print('*'*30)

# python 에서 False인 것들: 빈 것들, None, False, 0

# 14.6 연습문제
written_test=75
coding_test=True
if written_test>=80 and coding_test:
    print('합격')
else:
    print('불합격')

# 14.7 심사문제
# 89 72 93 82
grade=(list(map(int,input().split())))
print(grade)
average=sum(grade[:])/4

if -1<grade[0]<101 and -1<grade[1]<101 and-1<grade[2]<101 and -1<grade[3]<101:
    if average >=80:
        print('합격')
    else: print('불합격')
else: print('잘못된 점수')


























