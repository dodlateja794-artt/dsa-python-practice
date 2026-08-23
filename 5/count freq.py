s="programming"
seen={}
for ch in s:
    if ch in seen:
        seen[ch]+=1
    else:
        seen[ch]=1
print(seen)