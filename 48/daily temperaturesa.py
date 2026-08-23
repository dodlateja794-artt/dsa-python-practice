temperatures = [73,74,75,71,69,72,76,73]
answer=[0]*len(temperatures)
stack=[]
for i in range(len(temperatures)):
    while stack and temperatures[i]>temperatures[stack[-1]]:
        current=stack.pop()
        answer[current]=i-current
    stack.append(i)
print(answer)