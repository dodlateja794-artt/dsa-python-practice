arr = [3,5,2,1,7]
target = 8

seen = {}

for i in range(len(arr)):
    seen[arr[i]] = i

    diff = target - arr[i]

    if diff in seen:
        print(seen[diff], i)
    