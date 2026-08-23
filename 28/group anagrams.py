strs = ["eat","tea","tan","ate","nat","bat"]
seen={}
for word in strs:
    i=''.join(sorted(word))
    if i in seen:
        seen[i]+=[word]
    else:
        seen[i]=[word]
print(list(seen.values()))
