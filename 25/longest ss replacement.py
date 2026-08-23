s="AABAB"
k = 1
count={}
left=0
max_len=0
for right in range(len(s)):
    count[s[right]]=count.get(s[right],0)+1
    window_size=right-left+1
    max_freq=max(count.values())
    if window_size - max_freq>k:
        count[s[left]]-=1
        left+=1
    max_len=max(max_len,window_size)
print(max_len)
    