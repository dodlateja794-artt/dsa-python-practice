nums = [3, -1, 4, -2, 0, -5, 6]
result=[]
for i in nums:
    if i<0:
        result.append(i)
for i in nums:
    if i==0:
        result.append(i)
for i in nums:
    if i>0:
        result.append(i)
print(result)
