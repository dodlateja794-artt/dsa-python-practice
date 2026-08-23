strs = ["neet","code","love","you"]
result=""
for word in strs:
    length=len(word)
    result+=(str(length)+"#"+word)
print(result)