# ------------------------------------------------------------
# 제어문 중 조건문 살펴보기
# - 조건에 만족하는 경우 즉, True가 되면 실행되는 코드와
#   실행되지 않는 코드를 결정 하는 문법 
# - 형식
#   if 조건식:
#   ----실행코드 (들여쓰기 중요함! 들여쓰기 한애들만 if 조건식에 해당되는 코드!)
#   ----실행코드
#   코드 
# ------------------------------------------------------------
# [실습] 나이에 따른 대구 버스 요금 (현금값) 출력하기
# - 무료 : 0~5세까지
# - 500원: 6~12세까지
# - 1000원: 13~19
# - 1700원: 20~
# ------------------------------------------------------------
age=int(input("나이 : "))
bus=['무료','500원','1000원','1700원']

# 2개 경우 => 5세이하와 5세 초과
# if age <=5:
#     print(f'나이 {age}세는 버스요금이 {bus[0]}입니다.')
# else:
#     print(f'나이 {age}세는 버스요금이 {bus[1]}입니다.')


#4 개 경우 => 5세이하, 5세 초과~12세이하, 12세 초과~19세 이하, 20세 이상
if age <=5:
    print(f'나이 {age}세는 버스요금이 {bus[0]}입니다.')
if 5<age<=12:
    print(f'나이 {age}세는 버스요금이 {bus[1]}입니다.')
if 12<age<=19:
    print(f'나이 {age}세는 버스요금이 {bus[2]}입니다.')
if 20<=age: 
    print(f'나이 {age}세는 버스요금이 {bus[-1]}입니다.')

##----------------------------------------------------------------------------------
## => 다중조건문
## - 조건이 2개 이상인 경우
## - 형식 => 조건이 True인 경우 실행코드 실행 후 나머지 조건은 검사 X
##           조건이 False일 때만 아래 조건들 검사 진행
##    if 조건1:
##    ----실행코드
##    elif 조건2:
##    ----실행코드
##    elif 조건3:
##    ----실행코드
##       :
##    elif 조건n:
##    ----실행코드
##    else:
##    ----실행코드
##----------------------------------------------------------------------------------
if age <=5:
    print(f'나이 {age}세는 버스요금이 {bus[0]}입니다.')
elif age<=12:
    print(f'나이 {age}세는 버스요금이 {bus[1]}입니다.')
elif age<=19:
    print(f'나이 {age}세는 버스요금이 {bus[2]}입니다.')
#elif age>=20:
else: 
    print(f'나이 {age}세는 버스요금이 {bus[-1]}입니다.')


























