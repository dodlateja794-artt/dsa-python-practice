arr=[10,20,30,40]
first=arr[0]
second=arr[0]
for i in arr:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)
