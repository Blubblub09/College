import random
count = 0
repeat = 1
words = ["apple", "horse"]
word = random.choice(words)

#defines the function for the game turn
def wordle(word):
    global count
    global repeat
    result = "XXXXX"
    #user inputs guess and the guess counter increases by one
    guess = input("Enter 5 Letter Word: ").lower()
    count += 1

    #checks matches
    for letter in range(len(guess)):
        #Checks every letter in the word for matches before checking other conditions to prevent erroneous results
        if guess[letter] == word[letter]:
            #marks the letter as correct
            result = result[:letter] + "G" + result[letter+1:]
            #removes letter from word to ensure it cannot be used for later comparisons
            word = word[:letter] + "_" + word[letter+1:]

    #checks incorrect positions and 
    for letter in range(len(guess)):
        #Checks that this letter is not already marked as correct
        if word[letter] != "_":
            #checks if letter is in the word if not in the same position
            if guess[letter] in word:
                #marks the letter as in the wrong position
                result = result[:letter] + "Y" + result[letter+1:]
                word = word[:word.index(guess[letter])] + "_" + word[word.index(guess[letter])+1:]
            #resorts to narking the letter as incorrect if not present in the word
            elif word[letter] != "_":
                result = result[:letter] + "X" + result[letter+1:]

    #prints the result of the user's guess
    print(result)

    #checks if the user has correctly guessed the word
    if word == "_____":
        print(f"Congratulations!\n You found the correct word in {count} attempts!")
        repeat = 0

#Makes the turns repeat
while repeat == 1:
    wordle(word)

    if repeat == 0:
        choice = int(input("Do you want to play again? \n"
                           "1) Yes \n"
                           "2) No (Exit) \n"))

        if choice == 1:
            repeat = 1
            print("Good luck!")
            word = random.choice(words)
        else:
            print("Goodbye!")