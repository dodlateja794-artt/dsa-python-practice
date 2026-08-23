arr=[1,2,3,5,4]
sort=True
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        sort=False
        break
print(sort)