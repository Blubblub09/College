vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vCount = 0
cCount = 0
pwCount = 0


text = input("Enter a short section of text: \n").lower()

for char in text:
    if char in vowels:
        vCount = vCount + 1
    elif char in consonants:
        cCount = cCount + 1
    else:
        pwCount = pwCount + 1

print("Vowels:", vCount ,"Consonants:", cCount ,"Punctuation/Whitespace:", pwCount)