import random
count = 0
repeat = 1
words = ["apple", "horse"]
target = random.choice(words)

#defines the function for the game turn
def wordle(target):
    global count
    global repeat
    result = "XXXXX"
    #user inputs guess and the guess counter increases by one
    guess = input("Enter 5 Letter Word: ").lower()
    count += 1

    #checks matches
    for letter in range(len(guess)):
        #Checks every letter in the target for matches before checking other conditions to prevent erroneous results
        if guess[letter] == target[letter]:
            #marks the letter as correct
            result = result[:letter] + "G" + result[letter+1:]
            #removes letter from target to ensure it cannot be used for later comparisons
            target = target[:letter] + "_" + target[letter+1:]

    #checks incorrect positions and 
    for letter in range(len(guess)):
        #Checks that this letter is not already marked as correct
        if target[letter] != "_":
            #checks if letter is in the target word if not in the same position
            if guess[letter] in target:
                #marks the letter as in the wrong position
                result = result[:letter] + "Y" + result[letter+1:]
                target = target[:target.index(guess[letter])] + "_" + target[target.index(guess[letter])+1:]
            #resorts to marking the letter as incorrect if not present in the target word
            elif target[letter] != "_":
                result = result[:letter] + "X" + result[letter+1:]

    #prints the result of the user's guess
    print(result)

    #checks if the user has correctly guessed the target word
    if target == "_____":
        print(f"Congratulations!\n You found the correct target in {count} attempts!")
        repeat = 0

#Makes the turns repeat
while repeat == 1:
    wordle(target)

    if repeat == 0:
        choice = int(input("Do you want to play again? \n"
                           "1) Yes \n"
                           "2) No (Exit) \n"))

        if choice == 1:
            repeat = 1
            print("Good luck!")
            target = random.choice(words)
        else:
            print("Goodbye!")