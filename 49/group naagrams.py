strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
seen={}
for word in strs:
    words="".join(sorted(strs))
    if words in seen:
        seen[words].append(word)
    else:
        seen[words]=[word]
print(list(seen.values()))