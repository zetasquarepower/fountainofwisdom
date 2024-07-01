#문자열에 따옴표 포함 방법
s= 'Python isn\'t difficult'
print(s)

## 한글 문자열 출력이 안 될 때 ==> .py 파일을 utf-8이 아닌 cp949로 저장했기때문
## 따라서 메모장에서는 인코딩에서 utf-8을 선택 후 저장

# 9.3 연습문제, 심사문제
s='''Python is a programming language tht lets you work quickly
and 
integrate systems more effetively'''
print(s)

s='''\'Python\' is a "programming language" tht lets you work quickly
and 
integrate systems more effetively'''
print(s)

