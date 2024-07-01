#01.

#001
print('Hello World')
#002
print("Mary's cosmetics")
#003
print('신씨가 소리질렀다. "도둑이야".')
#004
print(r'C:\Windows')
#005
print("안녕하세요.\n만나서\t\t반갑습니다.")
#006
    #\n : 줄바꿈, \t : 탭
    #오늘은 일요일
#007
print('naver;kakao;sk;samsung')
#008
print(r'naver/kakao/sk/samsung')
#009
print("first",end=' ');print("second")
#010
print(5/3)

#02.
#011
삼성전자=50000
num=10
print(f'총 평가금액 : {삼성전자*num}')

#012
시가총액=298000000000000
현재가=50000
PER=15.79

#013
s = "hello"
t = "python"
print(f'{s}! {t}')

#014
    #8

#015
a="132"
print(type(a))
    # <class 'str'>

#016
num_str = "720"
print(int(num_str))

#017
num = 100
print(str(num))

#018
print(float("15.79"))

#019
year = "2020"
year=int(year)
print(year-1, year-2,year-3)

#020
monthlycost=48584
months=36
print(monthlycost*months)

#03.
#021
letters = 'python'
print(letters[0],letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number[:2], phone_number[4:8],phone_number[-4:])
#026
print(phone_number[:2], phone_number[4:8],phone_number[-4:], sep='')

#027
url = "http://sharebook.kr"
print(url[-2:])

#028
    # lang = 'python'
    # lang[0] = 'P'
    # print(lang)
    #Python 이 아니라 에러 뜬다함

#029
string = 'abcdfe2a354a32a'
string=string.replace('a', 'A')
print(string)

#030
    #aBcd

#031
    #34

#032
    #HiHiHi

#033
print('-'*80)
#034
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*4)

#035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %s \n이름: %s 나이: %s' % (name1,age1,name2,age2))

#036
print('이름: {} 나이: {} \n이름: {} 나이: {}'.format(name1,age1,name2,age2))

#037
print(f'이름: {name1} 나이: {age1}\n이름: {name2} 나이: {age2}')

#038
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',','')))

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#040
data = "   삼성전자    "
print(data.strip())

#041
ticker = "btc_krw"
ticker=ticker.upper()
print(ticker)

#042
ticker = "BTC_KRW"
ticker=ticker.lower()
print(ticker)

#043
print('hello'.capitalize())

#044
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#045
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls"))) #여기 괄호가 중요함!

#046
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#047
a = "hello world"
print(a.split())

#048
ticker = "btc_krw"
ticker1=ticker.split('_')
print(ticker1)

#049
date = "2020-05-01"
date=date.split('-')
print(date)

#050
data = "039490     "
data=data.rstrip()
print(data)
#051
movie_rank=['닥터 스트레인지','스플릿','럭키']

#052
movie_rank.append('배트맨')
print(movie_rank)

#053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank[:1]=['닥터 스트레인지','슈퍼맨']
print(movie_rank)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"슈퍼맨")

#054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[-2]
print(movie_rank)

#055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[-2:]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max: {max(nums)}\nmin: {min(nums)}')

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums[:]))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[-1])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

#069
string = "삼성전자/LG전자/Naver"
interest=string.split('/')
print(interest, type(interest))

#070
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

#071
my_variable=()

#072
movie_rank=('닥터 스트레인지','스플릿','럭키')
print(movie_rank)
#073
one=1,
print(one, type(one))

#074
# t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
    # 튜플은 변경이 불가능함

#075
    #튜플

#076
t = ('a', 'b', 'c')
t=list(t)
t[0]='A'
t=tuple(t)
print(t)

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

#079
    #apple banana cake

#080
ex=tuple(range(2,100,2))
print(ex)

#081
#082
#083
#084
#085
#086
#087
#088
#089
#090
#091
#092
#093
#094
#095
#096
#097
#098
#099
#100










































