s = "skya"
vowels="aeiouAEIOU"
found=False
for ch in s:
    if ch in vowels:
        found=True
        break
    else:
        found=False
print(found)
       
    