def fun():
    print("fun() called")

def disp():
    print("disp() called")

def msg():
    print("msg() called")

functions = [fun, disp, msg]
for f in functions:
    f()