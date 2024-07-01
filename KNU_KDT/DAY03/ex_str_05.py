#--------------------------------------------------
# 문자열 str 데이터 다루기 
# - 이스케이프문자 : 특수한 의미를 가지는 문자
#   * 형식 :\문자1개
#   * ' \n ' - 줄바꿈 문자
#   * ' \t ' - 탭간격 문자
#   * ' \' ' - 홑따옴표 문자
#   * ' \" ' - 쌍따옴표 문자
#   * ' \\ ' - \백슬래시 문자, 경로 (path), URL관련
#   * ' \U ' - 유니코드
#   * ' \a ' - 알람소리 문자 
#--------------------------------------------------

msg="오늘은 좋은 날\n내일은\n주말이라\n행복해"
print(f"msg 줄바꿈 : \n{msg}")

msg='오늘은 나의 \'생일\'이야'
print(msg)

file='C:\\Users\\kdp\\.azure\\test.txt'
print(file)
# r'  ' 또는 R'  ' : 문자열 내 이스케이프 문자는 무시됨!
# 경로, URL 문자열 처리에 자주 사용됨!
file=r'C:\Users\kdp\.azure\test.txt' #r stands for raw
print(file)

msg="Happy\tNew\tyear"
msg2=r"Happy\tNew\tyear"
print(msg,msg2)





























