# if조건문으로 특정 조건일때 코드 실행하기
x=10
if x==10:
    print('10이지롱')

# if에서 코드 생략하기
x=10
if x==10:
    pass #TODO: x가 10일때 처리가 필요함
# 이런 개발자 참고용인 일관된 키코드들: TODO, FIXME, BUG, NOTE etc

# 중첩 if 조건문

if x>= 10:
    print('10이상이지롱')
    if x==15:
        print('15입니뎅')
    if x==20:
        print('20임뎅')

# 13.6 연습문제
x=5
if x>0:
    print('ok')

# 13.7 심사문제
price=input()
coupon=input()
if coupon=='Cash3000':
    print(int(price)-3000)
elif coupon=='Cash5000':
    print(int(price)-5000)










