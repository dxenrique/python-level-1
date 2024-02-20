#user defined function that prints even number out of the list
def is_even(list):
    even_num=[]
    for i in list:
        if i%2==0:
            even_num.append(i)
    return even_num
even_num=is_even([2,3,42,51,62,70,5,9])
print("even numbers are :",even_num)