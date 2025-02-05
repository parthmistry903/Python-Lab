# Write a program that converts words present in a list into uppercase and stores them in a set.
def convertToUpperSet(wordsList):
    return {word.upper() for word in wordsList}

wordsList = ["hi", "hello"]
print(convertToUpperSet(wordsList))
