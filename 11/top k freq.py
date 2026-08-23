arr=[1,1,1,2,2,3]
k=2
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
keys=sorted(count.items(),key=lambda x:x[1],reverse=True)
result=[]
for key,values in keys[:k]:
    result.append(key)
print(result)