arr = [73,74,75,71,69,72,76,73]
stack=[]
answer=[0]*len(arr)
for i in range(len(arr)):
    while stack and arr[i]>arr[stack[-1]]:
        index=stack.pop()
        answer[index]=i-index
    stack.append(i)
print(answer)