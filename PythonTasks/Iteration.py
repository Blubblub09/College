lowerVowels = ["a", "e", "i", "o", "u"]
upperVowels = ["A", "E", "I", "O", "U"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
#Begins counts at 0 (uppervowels, lowervowels, consonants, punctuation/whitespace)
uvCount = 0
lvCount = 0
cCount = 0
pwCount = 0


text = input("Enter a short section of text: \n").lower()

#Counts the total vowels, consonants and punctuationwhitespace within the text
for char in text:
    if char in upperVowels:
        uvCount = uvCount + 1
    elif char in lowerVowels:
        lvCount = lvCount + 1
    elif char in consonants:
        cCount = cCount + 1
    else:
        pwCount = pwCount + 1

print("Uppercase Vowels:", uvCount ,"Lowercase Vowels:", lvCount ,"Consonants:", cCount ,"Punctuation/Whitespace:", pwCount)