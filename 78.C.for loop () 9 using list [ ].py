#program to print sum of elements in the list using for loop and also their product
#using list[ ]
t=0
n=[1,2,3,4,5,6]
for i in n:
    t=t+i
    print(t)
print("total sum is : ",t)
t=1
for i in n:
    t=t*i
print("total product is : ",t)