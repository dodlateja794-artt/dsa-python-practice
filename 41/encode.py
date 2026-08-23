strs=["teja","balu","sri","durga"]
result=""
for word in strs:
    length=len(word)
    result+=(str(length)+"#"+word)
print(result)