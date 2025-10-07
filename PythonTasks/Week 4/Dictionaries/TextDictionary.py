letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
charCount = {}
wordCount = {}


#Asks for target file name
name = input("Enter File Name: ")


#Reads file contents and saves to text variable
with open(name, "r") as file:
    text = file.read().lower().split()


for word in text:
    #Counts all letters in the text and adds them to a dictionary (Ignores punctuation and whitespace)
    for char in word:
        if char in letters:
            if char in charCount:
                charCount[char] = charCount[char] + 1
            else:
                charCount[char] = 1
    #Counts all words in the text and adds them to a dictionary
    if word in wordCount:
        wordCount[word] = wordCount[word] + 1
    else:
        wordCount[word] = 1


print(charCount)
print(wordCount)