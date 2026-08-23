arr=[1,2,3,4]
answer=[1]*len(arr)
left=1
for i in range(len(arr)):
    answer[i]=left
    left*=arr[i]
right=1
for i in range(len(arr)-1,-1,-1):
    answer[i]*=right
    right*=arr[i]
print(answer)