temps = [73,74,75,71,69,72,76,73]
stack=[]
answer=[0]*len(temps)
for i in range(len(temps)):
    while stack and temps[i]>temps[stack[-1]]:
        index=stack.pop()
        answer[index]=i-index
    stack.append(i)
print(answer)
