arr = [1, 3, 5, 3, 2, 5]
seen=set()
result=[]
for i in arr:
    if i not in seen:
        result.append(i)
print(result[-1])