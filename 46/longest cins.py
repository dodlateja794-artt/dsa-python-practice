arr=[1,34,2,45,3,4]
nums=set(arr)
seen={}
max_len=0
for i in nums:
    if i-1 not in nums:
        first=i
        length=1
        while first+1 in nums:
            first+=i
            length+=1
        max_len=max(max_len,length)
print(max_len)