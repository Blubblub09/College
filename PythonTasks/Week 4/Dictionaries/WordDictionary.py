wordCount = {}

text = input("Enter a section of text: ").lower().split()

#Counts all words in the text and adds them to the dictionary
for word in text:
    if word in wordCount:
        wordCount[word] = wordCount[word] + 1
    else:
        wordCount[word] = 1

print(wordCount)
