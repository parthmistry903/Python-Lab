# Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the target file.
import os
import sys
file1 = input("Enter first file name: ")
if not os.path.isfile(file1):
    print(f"{file1} doesn't exist.")
    sys.exit()
file2 = input("Enter second file name: ")
if not os.path.isfile(file2):
    print(f"{file2} doesn't exist.")
    sys.exit()
dest = input("Enter destination file name: ")
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(dest, 'w') as fw:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        if i < len(lines1):
            fw.write(lines1[i])
        if i < len(lines2):
            fw.write(lines2[i])