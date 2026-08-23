arr=[1,2,3,4,5]
total=0
prefix=[]
for i in arr:
    total+=i
    prefix.append(total)
print(prefix)