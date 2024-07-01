#입력값을 변수 두개에 저장하기 다음코드실행을 위해 주석으로 막음
##a,b=input('문자열 두개를 입력하세요:').split()
# print(a)
# print(b)

a,b=input('숫자 두개를 입력하세요:').split()
a=int(a)
b=int(b)
print(a+b)

##새로운내용*****************************************88
# map을 사용하여 정수로 변환하기
a,b=map(int,input('숫자 두개를 입력하세요:').split())
print(a+b)

a,b=map(int,input('숫자 두개를 입력하세요:').split(','))
print(a+b)