# ---------------------------------------------------------
# List 데이터 자료형 살펴보기
# - List와 메모리
# ----------------------------------------------------------
## List 생성 -----------------------------------------------

nums=[]
nums2=list([])
nums3=[]

print(f'nums의 id => {id(nums)}')
print(f'nums2의 id => {id(nums2)}')
print(f'nums3의 id => {id(nums3)}')
# 리스타가 처음 생성될때 별개의 장바구니가 생성됨******************
# 따라서 안의 객체 혹은 주소가 같을 때에도 리스트의 id/ 주소는 서로 다름
#-------------------------------------------------------
nums=[10,20]
nums2=list([10,20])
nums3=[10,20]

print(f'nums의 id => {id(nums)}')
print(f'nums[0]의 id => {id(nums[0])}')
print(f'nums[1]의 id => {id(nums[1])}')
print('*'*30)
print(f'nums2의 id => {id(nums2)}')
print(f'nums2[0]의 id => {id(nums2[0])}')
print(f'nums2[1]의 id => {id(nums2[1])}')
print(f'nums3의 id => {id(nums3)}')
##----------------
'''
nums의 id => 2940428422912
nums[0]의 id => 2940426480208
nums[1]의 id => 2940426480528
******************************
nums2의 id => 2940428798080
nums2[0]의 id => 2940426480208
nums2[1]의 id => 2940426480528
nums3의 id => 2940428430272
'''
##----------------------






















