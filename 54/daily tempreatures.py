temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
stack=[]
answer=[0]*len(temperatures)
for i in range(len(temperatures)):
    while  stack and temperatures[i]>temperatures[stack[-1]]:
        prev=stack[-1]
        answer[prev]=i-prev
        stack.pop()
    stack.append(i)
print(answer)