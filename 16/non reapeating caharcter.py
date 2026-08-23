arr = [1,2,2,3,4,4,5]
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for i in arr:
    if count[i]==1:
        print(i)
        break
        