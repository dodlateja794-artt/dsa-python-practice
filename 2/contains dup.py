arr=[1,2,3,1]
seen=[]
dup=[]
for i in arr:
    if i not in seen:
        seen.append(i)
    else:
        dup.append(i)
print(dup)