arr = [1,2,3,2,4,1]
result=[]
dup=[]
for i in arr:
    if i not in result :
        result.append(i)
    else:
        dup.append(i)
print(dup)