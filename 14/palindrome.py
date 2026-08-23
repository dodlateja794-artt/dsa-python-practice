n=12321
rev=0
original=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==original:
    print("palindrome")
else:
    print("not palindrome")