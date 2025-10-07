import random
names = []

#defining the function
def pick_winners(names, num_winners):
    #returns a random selection of winners
    return random.sample(names, k=num_winners)


#asks user for the amount of names they will input
repeat = int(input("How many names will be entered?   "))
#asks user to input the amount of names specified
for name in range(repeat):
    names.append(input("Enter a name:   "))

#asks the user for the amount of winners
num_winners = int(input("How many winners?  "))

#chooses and prints the winners
winners = pick_winners(names, num_winners)
print("The winners are:", winners)