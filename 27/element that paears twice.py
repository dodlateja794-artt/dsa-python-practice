arr = [1, 2, 3, 2, 4, 1,1]
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i,count in count.items():
    if count==2:
        print(i)
        break