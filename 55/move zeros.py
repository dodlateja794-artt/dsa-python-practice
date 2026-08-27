nums = [0, 1, 0, 3, 12]
i=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i]=nums[j]
        i+=1
for j in range(i,len(nums)):
    nums[j]=0
print(nums)
    