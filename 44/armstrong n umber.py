n=int(input("enter a number:"))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit**3
    n=n//10
if rev==original:
    print("armstrong")
else:
    print("not armstrong")
    
