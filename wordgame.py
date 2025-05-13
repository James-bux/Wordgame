import random

words = open("wordList.txt", "r")
lineofword = random.randint(1, 6394)

word = words.readline(lineofword)
lengthofword = len(word)
print(word)
print(lengthofword) #debugging prints
print(lineofword)
