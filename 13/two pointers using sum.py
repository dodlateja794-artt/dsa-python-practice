arr = [1,2,3,4,6,8]
target = 15
left=0
right=len(arr)-1
found=False
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        found=True
        break
    elif target>total:
        left+=1
    else:
        right-=1
print(found)
    