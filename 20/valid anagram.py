s = "race"
t = "care"
count={}
for ch in s:
    count[ch]=count.get(ch,0)+1
for ch in t:
    count[ch]-=1
for item in count.values():
    if item!=0:
        print("not anagram")
        break
else:
    print("anagram")
