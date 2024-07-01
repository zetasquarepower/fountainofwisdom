# --------------------------------------------------------
# List 데이터 자료형 살펴보기
# - List 와 str 
# ---------------------------------------------------------
msg="Happy"

# str => list 형변환
datas=list(msg)
print(datas)

msg=['Happy']
datas=list(msg) #[['Happy']] 이거 아니고 이거 =>['Happy']

datas1=list('Happy')
print(datas, datas1)
# 두가지 데이터 타입
#   -시퀀스 타입: 여러개의 데이터가 시퀀셜하게 있을 때 ex) list, str etc
#   -반복 가능 타입(iterable type) :list 와 str **int/float 절대 아님!!!!
