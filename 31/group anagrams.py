strs = ["eat","tea","tan","ate","nat","bat"]

result={}
for word in strs:
    words="".join(sorted(strs))
    if word in result:
        result[word].append(word)
    else:
        result[word]=[word]
print(list(result.values()))