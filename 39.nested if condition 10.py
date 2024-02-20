#comparing 3 numbers with nested if and elif condition
a=eval(input("enter number a :"))
b=eval(input("enter number b :"))
c=eval(input("enter number c :"))
if (a>b):
    if (a>c):
        print(a, " is largest ")
    else:
        print(c, " is largest")
elif(b>c):
    print(b,"is largest")
else:
    print(c, "is largest")
print("Thank You")