# 1. Print all alphabets in upper case and in lower case.
def Case():
    print("Uppercase Alphabets:", "".join([chr(i) for i in range(65, 91)]))
    print("Lowercase Alphabets:", "".join([chr(i) for i in range(97, 123)]))

Case()