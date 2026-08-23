arr=[1,2,3,4,5]
prefix=[]
total=0
for i in arr:
    total+=i
    prefix.append(total)
print(prefix)