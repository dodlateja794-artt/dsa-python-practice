n=6
prime=True
for i in range(2,n-1):
    if n%i==0:
        prime=False
        break    
print(prime)