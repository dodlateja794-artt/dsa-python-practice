nums = [3, 0, 1]
n = len(nums)
missing=n*(n+1)//2-sum(nums)
print(missing)