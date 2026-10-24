s = "aabbcdd"
seen={}
result=-1
for ch in s:
    if ch in seen:
        seen[ch]+=1
    else:
        seen[ch]=1
for key,value in seen.items():
    if value==1:
        result=key
        break
print(result)