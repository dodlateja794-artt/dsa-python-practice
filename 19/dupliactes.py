arr=[1,2,3,4,5,2]
seen=set()
for i in arr:
    if i in seen:
        print(i)
    else:
        seen.add(i)
print(seen)
         