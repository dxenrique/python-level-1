#factorial of input using recursive function
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the value of n: "))
print(factorial(n))