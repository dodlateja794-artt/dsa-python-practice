arr=[1,2,3]
seen=[]
for i in arr:
    if i in seen:
        print(True)
        break
    seen.append(i)
else:
    print(False)
