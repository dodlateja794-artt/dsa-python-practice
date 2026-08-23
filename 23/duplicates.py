arr = [1, 3, 5, 3, 2, 5]
seen=set()
dup=[]
for ch in arr:
    if ch not in seen:
        seen.add(ch)
    else:
        dup.append(ch)
        break
print(dup)
