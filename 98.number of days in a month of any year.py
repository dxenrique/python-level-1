a=int(input("enter year :"))
b=int(input("enter month :"))

if (b<12):
    if(b==2):
        if(a%4==0):
            print("month has 29 days :")
        else:
            print("month has 28 days :")
    elif(b==7 or b==1):
        print("month has 31 days :")
    elif b in [3,5,8,10,12]:
        print("month has 31 days :")
    else:
        print("month has 30 days :")
else:
    print("enter the number in range 1-12 :")