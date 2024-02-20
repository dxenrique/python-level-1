#program to print sum of elements in the list using for loop and also their product
#using range()
t=0     #for addition t=0
n=[1,2,3,4,5,6]
for i in range(0,6):     #or range(len(n))   #or range(6)
    t=t+n[i]
print("total sum is : ",t)
p=1       #for multiplication p=1
for i in range(0,6):    #or range(len(n))    #or range(6)
    p=p*n[i]
print("product is : ", p)