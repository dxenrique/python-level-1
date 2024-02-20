#if-condition and break inside for-loop
#print only till kishan
students=["ram","shyam","kishan","radha","radhika"]
for i in students:
    if i=="radha":
        break    #this expression will allow the program to terminate at radha
    print(i)    #this print is a part of for loop so under indentation