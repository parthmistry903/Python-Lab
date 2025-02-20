import os, sys

f = input()
if not os.path.isfile(f):
    sys.exit()
ch = word = line = 0
with open(f, "r") as f:
    for i in f:
        line+=1
        word = word + len(i.split())
        ch = ch + len(i.strip("\n"))
print(f"Lines: {line}, Words: {word}, Characters: {ch}")
