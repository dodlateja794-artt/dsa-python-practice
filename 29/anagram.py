s1 = "listen"
s2 = "silent"
count={}
for ch in s1:
    count[ch]=count.get(ch,0)+1
for ch in s2:
    count[ch]=count.get(ch,0)-1
for value in count.values():
    if value!=0:
        print(False)
        break
else:
    print(True)

        
        
