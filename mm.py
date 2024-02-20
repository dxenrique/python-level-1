def gcd(a,b):
    if a%b==0:
        return b
    else :
        return gcd(b,a%b)

a=int(input("enter first number"))
b=int(input("enter second number"))
print(gcd(a,b))
