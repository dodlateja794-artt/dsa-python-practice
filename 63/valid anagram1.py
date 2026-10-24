s = "listen"
t = "silent"
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
for ch in t:
    count[ch]=count.get(ch,0)-1
for key,value in count.items():
    if value==0:
        print(True)
    else:
        print(False)