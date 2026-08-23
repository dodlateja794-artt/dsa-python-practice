s="race: c'ar"
left=0
right=len(s)-1
while left<right:
    if not s[left].isalnum():
        left+=1
        continue
    if not s[right].isalnum():
        right-=1
        continue
    elif s[left].lower()!=s[right].lower():
        print(False)
        break
    left+=1
    right-=1
else:
    print(True)

    

        