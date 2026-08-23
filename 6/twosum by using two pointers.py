arr = [1,2,3,4,5,6]
target = 9
left=0
right=len(arr)-1
found=False
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        found=True
        break
    elif total<target:
        left+=1
    else:
        right-=1
print(found)