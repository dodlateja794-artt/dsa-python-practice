words=["teja","janu","sree","mad"]
decode=""
for word in words :
    decode+=str(len(word))+"#"+word
print(decode)