# Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.
import os
import sys
source = input("Enter source file name: ")
if not os.path.isfile(source):
    print(f"{source} doesn't exist.")
    sys.exit()
dest = input("Enter destination file name: ")
with open(source, 'r') as fr, open(dest, 'w') as fw:
    while True:
        ch = fr.read(1)
        if not ch:
            break
        fw.write(ch.upper())