nums=[1,0,4,0,5]
i=0
j=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i]=nums[j]
        i+=1
for j in range(i,len(nums)):
    nums[j]=0
print(nums)