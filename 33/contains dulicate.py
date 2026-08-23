nums = [1,2,3]
seen=set()
found=False
for i in nums:
    if i in seen:
        found=True
    seen.add(i)
print(found)
