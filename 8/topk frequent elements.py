nums = [1,1,1,2,2,3]
k = 2
count={}
for num in nums:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
items=sorted(count.items(),key=lambda x:x[1],reverse=True)
result=[]
for num,freq in items[:k]:
    result.append(num)
print(result)