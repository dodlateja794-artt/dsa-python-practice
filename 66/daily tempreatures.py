temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer=[-1]*len(temperatures)
stack=[]
for i in range(len(temperatures)):
    while stack and temperatures[stack[-1]]<temperatures[i]:
        prev=stack.pop()
        answer[prev]=i-prev
    stack.append(i)
print(answer)
    