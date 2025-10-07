import random

#defines the function for guessing a number
def guess_number():
    #sets guess to 0 to ensure the loop begins
    guess = 0
    #randomly determines the target number and sets the guess counter to 0
    target = random.randint(1, 20)
    count = 0

    print("I'm thinking of a number between 1 and 20...")

    #loops code until the user inputs the correct number
    while guess != target:
        #user inputs a guess and the counter increases by 1
        guess = int(input("Take a guess:    "))
        count += 1
        #determines if the user's guess was higher, lower, or equal to the target
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Well done! \n"
                  "You guessed it in {count} tries")


#defines the function for guessing a word
def guess_word():
    #defines possible words and picks a random word to be the target
    words = ["apple", "avocado", "banana", "blackberry", "cherry", "coconut"]
    target = random.choice(words)

    #defines the possible clues to give when the use is incorrect
    hints = [f"The word begins with {(target[0])}",
             f"The word has {(len(target))} letters"]
    
    #sets the guess to "" to ensure the loop begins
    guess = ""
    while guess != target:
        guess = input("Guess a fruit:   ").lower()

        #determines if the guess is equal to the target, if not, provides a hint
        if guess == target:
            print(f"Correct! \n"
                  "The secret word was {target}")
        else:
            print(f"Nope! \n"
                  "Hint: {random.choice(hints)}")
            
guess_word()


