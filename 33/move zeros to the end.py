nums = [0,1,0,3,12,0]
result=[]
for i in nums:
    if i !=0:
        result.append(i)
zero_count=nums.count(0)
for i in range(zero_count):
    result.append(0)
print(result)