arr = [4, 5, 4, 6, 5, 7]
count={}
for ch in arr:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
for ch,count in count.items():
    if count==1:
        print(ch)
        break