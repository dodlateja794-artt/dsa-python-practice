s = "I love Django"
count=0
left=0
for ch in s:
    if not s[left].isalnum():
        count+=1
    left+=1
print(count+1)