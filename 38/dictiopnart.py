s = "swiss"
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
for ch,value in count.items():
    if count[ch]==1:
        print(ch)
        break
            