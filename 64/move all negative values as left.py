arr = [3, -2, 5, -7, 8, -1, 4,0]
result=[]
for i in arr:
    if i<=0:
        result.append(i)
for i in arr:
    if i>0:
        result.append(i)
print(result)