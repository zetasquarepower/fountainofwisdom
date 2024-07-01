#객체가 같은지 다른지 비교하기
print(f'1==1.0 : {1==1.0}')

print(f'1 is 1.0 : {1 is 1.0}')

print(f'1 is not 1.0 : {1 is not 1.0}')

#******중요*********
#값 비교에 is 쓰지않기!!!!!! 메모리 주소가 달라질 수 있어 다른 객체가 되므로
#값이 같더라고 is 로 비교하면 False가 나옴! 값을 비교할 때는 is가 아닌 비교 연산자를 사용해야함!

a=-5
print(f'a is -5 :{a is -5}')

a=-6
print(f'a is -6 :{a is -6}')

print(f'((not True) and False) or (not False)  :  {((not True) and False) or (not False)}')

#주의할점
print(f'not 1 is 1.0  :  {not 1 is 1.0}') ##이때 (1 is 1.0) 부터하고 그다음에 not 을 해당시킴

#8.4 연습문제, 심사문제
korean=92
english=47
mathematics=86
science=81
print(korean>=50 and english>=50 and mathematics>=50 and science>=50)

korea, english, maths, sciences=map(int,input().split())
print(korean>=90 and english>80 and mathematics>85 and science>=80)
