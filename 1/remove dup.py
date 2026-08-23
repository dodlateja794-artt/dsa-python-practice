arr=[1,2,3,2,1]
dup=[]
for i in arr:
    if i not in dup:
        dup.append(i)
print(dup)