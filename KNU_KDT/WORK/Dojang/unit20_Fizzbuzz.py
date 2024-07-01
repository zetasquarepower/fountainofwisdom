# 1. 1에서 100까지 출력
for i in range(1,101):
    print(i)

# 2. 3의 배수는 Fizz 출력
# 3. 5의 배수는 Buzz 출력
for i in range(1,101):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)

# 4. 3과 5의 공배수는 FizzBuzz 출력

for i in range(1,101):
    if i%3==0 and i%5==0: ##공배수 먼저 검사!!!!
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)

#another way of finding 3과 5의 공배수는 FizzBuzz 출력

for i in range(1,101):
    if i%15==0: ##공배수 먼저 검사!!!!
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)

# 코드 단축하기
for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)

# 연습문제:2와 11의 배수, 공배수 처리하기
for i in range(1,101)
