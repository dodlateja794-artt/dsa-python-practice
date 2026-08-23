s1="listen"
s2="silent"
count={}
for ch in s1:
    count[ch]=count.get(ch,0)+1
for  ch in s2:
    if ch not in count:
        print(False)
        break
    count[ch]-=1
else:
    for val in count.values():
        if val!=0:
            print(False)
            break
    else:
        print(True)