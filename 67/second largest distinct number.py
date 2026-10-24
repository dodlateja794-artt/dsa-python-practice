nums = [10, 5, 8, 10, 3, 8]
arr=[]
for i in nums:
    if i not in arr:
        arr.append(i)
largest=float("-inf")
second=float("-inf")
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)

