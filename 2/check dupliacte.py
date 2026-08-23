arr=[1,2,3,4]
seen=[]
for i in arr:
    if i in seen:
        print(False)
        break
    seen.append(i)
else:
    print(True)