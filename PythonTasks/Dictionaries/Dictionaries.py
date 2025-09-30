letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
charCount = {}

text = input("Enter a section of text: ").lower().strip()

#Counts all letters in the text and adds them to the dictionary
#Ignores punctuation and whitespace
for char in text:
    if char in letters:
        if char in charCount:
            charCount[char] = charCount[char] + 1
        else:
            charCount[char] = 1

print(charCount)