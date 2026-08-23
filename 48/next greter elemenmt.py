nums= [1, 3, 4, 2]
answer=[0]*len(nums)
stack=[]
for i in range(len(nums)):
    while stack and nums[i]>stack[-1]:
        current=stack.pop()
        answer[i]=i-current
    stack.append(i)
print(answer)


    
        
