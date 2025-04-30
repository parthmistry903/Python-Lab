#1.	Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.

def fun():
    print("fun() called")

def disp():
    print("disp() called")

def msg():
    print("msg() called")

functions = [fun, disp, msg]
for f in functions:
    f()