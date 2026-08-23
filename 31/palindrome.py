s = "madam"
left=0
right=len(s)-1
palindrome=True
for ch in s:
    if s[left]!=s[right]:
        palindrome=False
    else:
        left+=1
        right-=1
print(palindrome)
        
    


        