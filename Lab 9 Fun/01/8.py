# Write a program that defines a function convert() that receives a string containing a sequence of
# whitespace separated words and returns a string after removing all duplicate words and sorting them
# alphanumerically. Hint: use set(), list () , sorted(), join().
def convert(s):
    words = s.split()
    setW = set(words)
    l = sorted(setW)
    return " ".join(l)

s = "a b a c"
print(convert(s))
