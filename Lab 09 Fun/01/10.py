# Write a program that defines a function called frequency() which computes the frequency of words 
# present in a string passed to it. The frequencies should be returned in sorted order of words in 
# the string.
def frequency(s):
    l=s.split()
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    # for i in l:              # Without .get
    #     if i in d:
    #         d[i] += 1
    #     else:
    #         d[i] = 1
    return dict(sorted(d.items()))
    # return dict(sorted(d.items(), key=lambda item: item[1]))  # Sort by values


s = "apple banana apple orange apple"
print(frequency(s))