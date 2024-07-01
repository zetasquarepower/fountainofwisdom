##bool()은 값이 있으면 무조건 True // 정수 0, 실수 0.0, 문자열'' , ""제외한 모든것이 True
print(f''' {bool(1)}
{bool('False')}
      ''')

############이상하다 이거 봐#######
print(f'True and "Python"  :  {True and "Python"}') #마지막 단락평가한 값 반환!!
print(f'"Python" and True  :  {"Python" and True}') #앞 python=True
print(f'"Python" and False  :  {"Python" and False}')
print(f'False and "Python"  :  {False and "Python"}') #false가 단락지으므로 첫번째 값 반환
print(f'0 and "Python"  :  {0 and "Python"}') #0이 단락지으므로 첫번째 값 반환
print(f'True or "Python"  :  {True or "Python"}') #첫번째값 반환
print(f'"Python" or True  :  {"Python" or True}') #첫번째값 반환
print(f'False or "Python"  :  {False or "Python"}') #두번째값 반환
print(f'"Python" or False  :  {"Python" or False}') #두번째값 반환

#reference count
import sys
print(sys.getrefcount(1000))
x=1000
print(sys.getrefcount(1000))
y=1000
print(sys.getrefcount(1000))
print(x is y)

#행렬 곱셈 연산자
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a@b)