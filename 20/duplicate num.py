arr=[1,2,3,4,5,2]
seen=set()
dup=[]
for i in arr:
    if i in seen:
        dup.append(i)
    else:
        seen.add(i)
print(dup)