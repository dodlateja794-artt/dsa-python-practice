n=input("enter a name:")
vowels="AEIOUaeiou"
count=0
for ch in n:
    if ch in vowels:
        count+=1
print(count)