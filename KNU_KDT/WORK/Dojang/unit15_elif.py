#15. elif 사용하여 여러 방향으로 분기하기

button=int(input())
if button==1:
    print('콜라')
elif button==2:
    print('사이다')
elif button==3:
    print('환타')
else: print('제공하지 않는 메뉴')

# 15.3 연습문제 
x=int(input())
if 10<x<21: print('11~20')
elif 20<x<31: print('21~30')
else: print('아무것도 해당하지 않음')

# 15.4 심사문제 
age=int(input())
balance=9000
if 7<=age<=12:
    print(balance-650)
elif 13<=age<=18:
    print(balance-1050)
else: print(balance-1250)


