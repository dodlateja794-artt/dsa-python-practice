a = [1,2,3,4]
b = [3,4,5,6]
result=[]
for ch in a:
    if ch in b:
        result.append(ch)
print(result)