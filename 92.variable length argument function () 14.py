#variable length argument user defined function
def addition(*numbers):
    total=0
    for i in numbers :
        total=total+i
    print("sum is :",total)
addition()      #function call
addition(10,5,2,5,4)      #function call
addition(78,7,2,5)      #function call