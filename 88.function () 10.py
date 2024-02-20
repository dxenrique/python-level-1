#write a program to find a out  the factorial of a number using funtion and user input

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the value of n : "))
print(fact(n))