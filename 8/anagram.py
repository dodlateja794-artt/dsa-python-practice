s1="listen"
s2="silent"
count={}
for ch in s1:
    count[ch]=count.get(ch,0)+1
for ch in s2:
    count[ch]=count.get(ch,0)-1
for val in count.values():
    if val!=0:
        print("not anagram")
        break
else:
    print("anagram")
