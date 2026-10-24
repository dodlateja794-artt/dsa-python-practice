arr = [3, -2, 5, -7, 8, -1, 4]
result=[]
i=0
for j in range(len(arr)):
    if arr[j]<0:
        arr[i]=arr[j]
        i+=1
        result.append(i)
print(result)