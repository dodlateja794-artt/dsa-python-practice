def greter_nums(nums):
    stack=[]
    result=[-1]*len(nums)
    for i in range(2*len(nums)):
        current=i%len(nums)
        while stack and nums[stack[-1]]<nums[current]:
            index=stack.pop()
            result[index]=nums[current]
        if i<len(nums):
            stack.append(current)
    return result
print(greter_nums([1,2,1]))