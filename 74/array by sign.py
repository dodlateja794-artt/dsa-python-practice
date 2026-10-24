nums = [3, 1, -2, -5, 2, -4]
positive=0
negative=1
result=[0]*len(nums)
for i in range(len(nums)):
    if nums[i]>0:
        result[positive]=nums[i]
        positive+=2
    else:
        result[negative]=nums[i]
        negative+=2
print(result)
