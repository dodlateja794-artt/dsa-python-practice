s = "aabbcddee"
seen={}
for ch in s:
    if ch in seen:
        seen[ch]+=1
    else:
        seen[ch]=1
for ch in s:
    if seen[ch]==1:
        print(ch)
        