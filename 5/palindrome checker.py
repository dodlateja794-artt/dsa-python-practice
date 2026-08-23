arr=[1,2,3,2,1]
left=0
right=len(arr)-1
palindrome=True
while left<right:
    if arr[left]!=arr[right]:
        palindrome=False
        break
    left+=1
    right-=1
print(palindrome)

