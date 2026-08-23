arr = [1,1,2,3,3,4,4]
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in arr:
    if count[i]==1:
        print(i)