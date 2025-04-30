# Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.
import os
import sys
source = input("Enter source file name: ")
if not os.path.isfile(source):
    print(f"{source} doesn't exist.")
    sys.exit()
dest = input("Enter destination file name: ")
with open(source, 'r') as fr, open(dest, 'w') as fw:
    for line in fr:
        words = line.split()
        new_words = [word for word in words if word.lower() not in ['a', 'the', 'an']]
        new_line = ' '.join(new_words) + '\n'
        fw.write(new_line)