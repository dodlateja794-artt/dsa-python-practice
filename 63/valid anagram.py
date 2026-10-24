s = "listen"
t = "silent"
seen={}
count={}
for ch in s:
    if ch in seen:
        seen[ch]+=1
    else:
        seen[ch]=1
for ch in t:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
if seen==count:
    print(True)
else:
    print(False)
