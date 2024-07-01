#18. break, continue로 반복문 제어하기

i=0
while True:
    print(i)
    i+=1
    if i==100: break

# for
for i in range(100):
    print(i)
    if i ==10:
        break

#continue로 코드 실행 건너뛰기 :for

for i in range(1000):
    if i%2==0: # 짝수라면 continue, 짝수라면 실행하지말고건너뛰라==홀수만 프린트해라
        continue
    print(i)

#continue로 코드 실행 건너뛰기 :while
i=0
while i <100:
    i+=1
    if i%2==0:
        continue # 짝수라면 continue, 짝수라면 실행하지말고건너뛰라==홀수만 프린트해라
    print(i)

# pass
for i in range(10):
    pass # 아무일도 하지않음

# 입력 횟수만큼 반복
# cnt=int(input('반복횟수please'))
# i=0
# while True:
#     print(i)
#     i+=1
#     if i==cnt: break

# 입력된 숫자 포함해서 홀수 출력
# count=int(input('반복할 횟수:'))
# for i in range(count+1):
#     if i%2==0:
#         continue
#     print(i)

## simply, break==>반복문끝내기, continue==>아래 코드 건너뛴 다음 계속 반복

# 18.5 연습문제 ***

i=0
while True:
    if i%10 !=3:
        i+=1
        continue
    if i>73: break
    print(i, end=' ' )
    i+=1

#18.6 심사 문제
a,b=map(int,input().split())
while True:
    if a>b:
        break
    print(a,end=' ')
    a+=1




