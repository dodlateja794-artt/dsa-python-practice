s = "aabbbcc"
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
max_char=""
max_count=0
for ch in count:
    if count[ch]>max_count:
        max_count=count[ch]
        max_char=ch
print(max_char)
    
