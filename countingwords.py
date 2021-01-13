introString = input("Enter your introduction")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount + 1
    if (i==" "):
        wordCount = wordCount + 1
print("Number of words in this string")
print(wordCount)
print("Number of characters in this string")
print(characterCount)