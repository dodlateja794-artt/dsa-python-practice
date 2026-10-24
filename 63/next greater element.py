arr = [4, 5, 2, 10, 8]
stack=[]
answer=[-1]*len(arr)
for i in range(len(arr)-1,-1,-1):
    while  stack and stack[-1]<=arr[i]:
        stack.pop()
    if stack==[]:
        answer[i]=-1
    else:
        answer[i]=stack[-1]
    stack.append(arr[i])
print(answer)
        