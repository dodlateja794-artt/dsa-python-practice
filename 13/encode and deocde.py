s=["cat","apple","monkey"]
decode=""
for i in s:
    decode+=str(len(i))+"#"+i
print(decode)