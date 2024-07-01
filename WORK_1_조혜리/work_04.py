#sep 사용
print(1,2,3, sep=', ')
print(4,5,6, sep='**')
print('hello',2,'python', sep='')
print(9383626,2,3, sep='x')
print('hello',2,'python', sep='\n')
# escape sequence \t:tab키같은효과, \\: '\' 문자 자체 출력할 때 쓰임

#end 사용
print(1,2,3, end=', ')
print(4,5,6, end='**')
print('hello',2,'python', end='')
print(9383626,2,3, end='             ')
print('hello',2,'python', end='\n') #default와 같은 효과

#7.4 연습문제, 심사문제
year=2000
month=10
day=27
hour=11
minute=43
second=59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':' )

year, month, day, hour, minute, second=input().split()
print(year,month,day,sep='-',end='')
print('T', end='')
print(hour,minute,second, sep=':')