strs = ["eat","tea","tan","ate","nat","bat"]
seen={}
for word in strs:
    key=''.join(sorted(word))
    if key in seen:
       seen[key].append(word)
    else:
        seen[key]=[word]
print(list(seen.values()))
