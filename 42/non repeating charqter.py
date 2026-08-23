arr = [4, 5, 1, 2, 1, 4, 5]
seen={}
for i in arr:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for i in arr:
    if seen[i]==1:
        print(i)