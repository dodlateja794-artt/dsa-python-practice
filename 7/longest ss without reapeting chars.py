a="abcabcbb"
left=0
max_len=0
seen=set()
for right in range(len(a)):
    while a[right] in seen:
        seen.remove(a[left])
        left+=1
    seen.add(a[right])
    max_len=max(max_len,right-left+1)
print(max_len)

