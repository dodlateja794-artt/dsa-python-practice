arr = [12, 45, 7, 34,45, 20]
largest=arr[0]
second=arr[0]
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)
