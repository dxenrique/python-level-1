x = "awesome"
counter = 0

def myfunc():
    global counter
    counter += 1
    if counter <= 1:
        print("Python is " + x)
        myfunc()

myfunc()
