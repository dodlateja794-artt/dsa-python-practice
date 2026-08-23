arr = [0, 1, 0, 3, 12]
result=[]
for i in arr:
    if i!=0:
        result.append(i)
zeros=arr.count(0)
for i in range(zeros):
    result.append(0)
print(result)