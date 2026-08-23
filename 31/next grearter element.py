nums = [2,1,2,4]
stack=[]
answer=[-1]*len(nums)
for i in range(len(nums)):
    while stack and nums[i]>nums[stack[-1]]:
        index=stack.pop()
        answer[index]=nums[i]
    stack.append(i)
print(answer)