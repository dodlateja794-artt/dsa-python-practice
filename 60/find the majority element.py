nums = [2,2,1,1,1,2,2]
n=7
count={}
for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for key,value in count.items():
    if value>n/2:
        print(key)