s = "abcabcbb"
seen=set()
left=0
max_lenght=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    max_lenght=max(max_lenght,right-left+1)
print(max_lenght)
