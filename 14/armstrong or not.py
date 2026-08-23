n=153
total=0
original=n
while n>0:
    digit=n%10
    total=total+digit**3
    n=n//10
if total==original:
    print("armstrong")
else:
    print("not armstrong")