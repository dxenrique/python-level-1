#calculator using elif
a=eval(input("enter number a :"))
b=eval(input("enter number b :"))
c=input("enter operators :(+,-,*,/) : ")
if c=="+":
    print("sum is : ", a+b)
elif c=="-":
    print("subtraction is : ", a-b)
elif c=="*":
    print("product is : ", a*b)
elif c=="/":
    print("division is : ",a/b)
else:
    print("operation not found")
print("Thank You")