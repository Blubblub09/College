import math
numbers = [["Number", "Floor", "Ceil", "Trunc"]]

#Asks the user how many numbers they are going to round
repeats = int(input("How many numbers?  "))

#repeats to input more numbers
for i in range(repeats):
    #prompts user with numbered input
    number = float(input(f"Enter number {str(i+1)}:   "))

    #Adds numbers to the list
    numbers.append([number, math.floor(number), math.ceil(number), math.trunc(number)])

#prints each row of the table on new lines
for row in numbers:
    print(row)