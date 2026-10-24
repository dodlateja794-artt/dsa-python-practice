nums = [4, 5, 2, 10, 8]
stack=[]
result=[-1]*len(nums)
for i in range(len(nums)):
    while stack and nums[stack[-1]]<nums[i]:
        current=stack.pop()
        result[i]=max(current,nums[i])
    stack.append(i)
print(result) 