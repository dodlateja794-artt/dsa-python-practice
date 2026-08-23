arr=[1,2,3,4,5]
target=7
found=False
for i in range(len(arr)):
    if target==arr[i]:
        found=True
print(found)