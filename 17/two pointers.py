arr=[1,2,3,4,5]
target=9
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(True)
        break
    elif target>total:
        left+=1
    else:
        right-=1
else:
    print(False)