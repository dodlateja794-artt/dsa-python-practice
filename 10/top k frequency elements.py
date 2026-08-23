nums=[1,1,1,2,2,3]
k=2
count={}
for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
keys=sorted(count.items(),key=lambda x:x[1],reverse=True)
result=[]
for key,value in keys[:k]:
    result.append(key)
print(result)
    
    
