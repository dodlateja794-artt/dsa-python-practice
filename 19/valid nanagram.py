s = "listen"
t = "silent"
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
for ch in t:
    count[ch]-=1
for value in count.values():
    if value!=0:
        print("not anagram")
        break
else:
    print("anagram")