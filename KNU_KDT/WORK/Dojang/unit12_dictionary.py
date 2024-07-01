lux={'health':490, 'health':800,'mana':334, 'melee':550, 'armor':18.72}
print(lux['health'])
# 중복 키는 뒤에꺼만 사용됨
x={100:'hundred',False:0, 3.5:[3.5,3.5]}
print(x) # 키에는 리스트와 딕셔너리 사용불가, 값에는 가능

#빈 딕셔너리 
dic1={}
dic2=dict()
print(dic1,dic2)

#dict()으로 딕셔너리 만드는 법
lux1=dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

# dict 에서 zip()이용하기
lux2=dict(zip(['health', 'mana', 'melee', 'armor'],[490,334,550,18.72]))
print(lux2)

# 리스트 안에 (키, 값)형식의 튜플 나열하기
# dict(  [   (),(),()  ]   )
lux3=dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)

# dict 안에서 중괄호로 딕셔너리 생성법
lux4=dict({'health':490, 'health':800,'mana':334, 'melee':550, 'armor':18.72})
print(lux4)
print(lux4['health'], type(lux4['health'])) # <class 'int'>

# 해당 키의 값 변경하기
lux4['health']=1
print(lux4['health']) #1

lux4['health']='헤헿'
print(lux4['health']) #헤헿

# 없는 키에 추가 하면 키랑 값이랑 같이 추가 생성됨
lux4['power']='만땅'
print(lux4) # {'health': '헤헿', 'mana': 334, 'melee': 550, 'armor': 18.72, 'power': '만땅'}

# 키 in 딕셔너리 in / not in
print('power' in lux4) #True

#딕셔너리는 해시(Hash) 기법을 이용해서 데이터 저장
# 키-값 형태의 자료형을 해시, 해시 맵, 해시 테이블 로 부름

#len(dictionary)
print(len(lux4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ))

# 12.4 연습문제
camille={
'health':575.6,
'health_regen':1.7,
'mana':338.8,
'mana_regen':1.63,
'melee':125,
'attack_damage':60,
'attack_speed':0.625,
'armor':26,
'magic_resistance':32.1,
'movement_speed':340
}

print(camille['health'], camille['movement_speed'])

# 12.5 심사문제
# *************** zip()사용하기! ********************
key1=input().split()
values1=input().split()
dict1=dict(zip(key1,values1))
print(dict1)























