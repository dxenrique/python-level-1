#"if" and "continue" inside for-loop
#print all except kishan
students=["ram","shyam","kishan","radha","radhika"]
for i in students:
    if i=="kishan":
        continue   #this expression will allow the program to ignore kishan
    print(i)
