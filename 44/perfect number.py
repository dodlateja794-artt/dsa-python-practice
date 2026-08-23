n=123
total=0
for i in range(1,n):
    if n%i==0:
        total+=i
if total==n:
    print("perfect")
else:
    print("not perfect")