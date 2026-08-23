arr=[1,2,3,4,1,2]
seen={}
for i in arr:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
print(seen)