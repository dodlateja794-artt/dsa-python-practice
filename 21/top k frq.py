nums = [1,1,1,2,2,3]
k = 2
count={}
for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
values=sorted(count.items(),key=lambda x:x[1],reverse=True)
for key,val in values[:k]:
    print(key)      
    