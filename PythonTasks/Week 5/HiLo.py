import random

#defines the function for guessing a number
def guess_number():
    #sets guess to 0 to ensure the loop begins
    guess = 0
    #randomly determines the target number and sets the guess counter to 0
    target = float(str(random.uniform(1, 20))[:-13])
    count = 0

    print("I'm thinking of a number between 1 and 20...")

    #loops code until the user inputs the correct number
    while guess != target:
        #user inputs a guess and the counter increases by 1
        guess = float(input("Take a guess:    "))
        count += 1
        #determines if the user's guess was higher, lower, or equal to the target
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Well done! \nYou guessed it in {count} tries")


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
            #informs the user they've won and confirms the target word
            print(f"Correct! \nThe secret word was {target}")
        else:
            #chooses and outputs a hint
            hint = random.choice(hints)
            print(f"Nope! \nHint: {hint}")
            

#defining the function of the menu
def menu():
    #Getting the user's input
    try:
        choice = int(input("Welcome to the menu, please select an option:\n"
                           "1) Guess the number\n"
                           "2) Guess the letter\n"
                           "3) Exit\n"))
    except:
        print("Please enter an integer value")
        menu()
        
    #Determining the route of the user, or repeating if they have given an erroneous input
    if choice == 3:
        print("Goodbye!")
    elif choice == 1 or choice == 2:
        print("Good luck!")
        if choice == 1:
            guess_number()
            menu()
        elif choice == 2:
            guess_word()
            menu()
    else:
        print("Please enter a number between 1 and 3")
        menu()

menu()