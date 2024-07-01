# 19. 계단식으로 별 출력하기

#중첩 루프 사용
# 변수명: i, j 사용관례==>i 먼저, 바깥쪽 세로처리코드 / j 다음, 안쪽 가로처리코드
for i in range(5):
    for j in range(5):
        print('j:',j,sep='', end=' ')
    print('i:',i,'\\n',sep='')

#사각형으로 별 출력
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

#사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*',end='')
    print() # 그냥 줄바꿈

# 계단식으로 별 출력
for i in range(5):
    for j in range(5):
        if j<=i: ##==세로방향변수 i만큼
            print('*',end='')
    print()

# 대각선으로 별 출력

    #아래가 일직선인 이유: 출력이 안되면 공백이아니라 그냥 공간이 없음
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')
    print()

    #대각선: 공백을 출력해주면 대각선됨
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')
        else: print(' ',end='')
    print()

#19.5 연습문제
for i in range (5):
    for j in range(5):
        if j>=i:
            print('*',end='')
        else: print(' ', end='')
    print()

#19.6 심사문제
# 어렵다 반씩 쪼개서 하기
height=int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j>i:
            print(' ',end='')
        else:print('*',end='')
    for j in range(height):
        if j<i:
            print('*',end='')
    print()





