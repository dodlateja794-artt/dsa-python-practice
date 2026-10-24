nums = [1, 2, 3, 4]
answer=[-1]*len(nums)    #store the -1 as if the answer is null
left=1
for i in range(len(nums)):   #from left to right
    answer[i]=left
    left*=nums[i]
right=1
for i in range(len(nums)-1,-1,-1):   #from right to left multiplication
    answer[i]*=right
    right*=nums[i]
print(answer)

