# 14.7 심사문제
# 89 72 93 82
grade=(list(map(int,input().split())))
print(grade)
average=sum(grade[:])/4
k,e,m,s=grade
print(k)

# if -1<grade[0]<101 and -1<grade[1]<101 and-1<grade[2]<101 and -1<grade[3]<101:
#     if average >=80:
#         print('합격')
#     else: print('불합격')
# else: print('잘못된 점수')

height=int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j>i:
            print(' ',end='')
        else:print('*',end='')
    for j in range(height):
        if j<1:
            print('*',end='')
    print()
