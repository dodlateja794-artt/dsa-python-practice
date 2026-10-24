nums = [2, -1, 4, -3, 5, -2]
result=[]
for i in nums:
    if i>0:
        result.append(i)
i=0
for j in range(len(nums)):
    if nums[j]<0:
        nums[i]=nums[j]
        i+=1
for j in range(i,len(nums)):
    


        