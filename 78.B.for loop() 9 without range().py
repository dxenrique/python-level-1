#program to print sum of elements in the list using for loop and also their product
# without using range()
n=[1,2,3,4,5,6]
r=0     #for addition
m=1     #for multiplication
for i in n:
    r=r+i
    m=m*i
print("sum is : ", r)
print("producr is : ",m)