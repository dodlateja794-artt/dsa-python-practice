nums = [1,1,1,2,2,3]
k = 2
seen={}
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
sorted_item=sorted(seen.items(),key=lambda x:x[1],reverse=True)
result=[]
for num,freq in sorted_item[:k]:
    result.append(num)
print(result)

