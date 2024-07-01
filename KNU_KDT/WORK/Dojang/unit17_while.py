#17. while 반복문으로 hello, world 100번 출력하기

i=0
while i <100:
    print('hello, world')
    i+=1

# 참고할만한 error code: invalid syntax==>:콜론 체크! / indented block==>indentation체크!

i=1
while i<=100:
    print('hello world')
    i+=1

i=100
while i>0:
    print('hello world')
    i-=1

# count=int(input())
# i=0
# while i<count:
#     print('hello world')
#     i+=1

# count=int(input())
# while count>0:
#     print('hello world')
#     count-=1  input막음

# random module
import random

print(random.random()) #returns random number 0.6029358944661753

# .randint(a, b) 함수 -->(random integer)
# a 와 b 사이의 random number 줌
print(random.randint(1,6))

#-------------------------------------
import random
i=0
while i != 3:
    i=random.randint(1,6)
    print(i)
# 3이 나올때 까지 실행됨----------------

#random.choice(시퀀스객체)
dice=[1,2,3,4,5,6]
print(random.choice(dice))

# while로 무한루프 생성

# while True:
#     print('neverending') ==>ctrl+c하면 멈춤 휴
# True 대신 True로 취급되는 0이 아닌 숫자, 비지않은 문자열을 넣어도 무한루프 됨

# 17.5 연습문제 
i=2
j=5
while i <=32 or j>0:
    print(i, j)
    i=i*2
    j=j-1

# 17.6 심사문제 
amount=int(input())
cost1=1350
while amount>=1350:
    amount=amount-cost1
    print(amount)


