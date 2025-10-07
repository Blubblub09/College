import math

#Defines the function
def is_square(n):
    #determines if n is a square number by comparing the root to itself with any decimals cut off
    #if both numbers are equal then n is a perfect square
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False

#num set to -1 to ensure the loop begins
num = -1
#loops code untill user inputs 0
while num != 0:
    #user prompted to enter a number, and given the method of quitting
    num = int(input("Enter a number (0 to quit):    "))
    #determines if exiting first to skip checks if true
    if num == 0:
        print("Goodbye!")
    #checks if num is a square number using the function
    #uses the function's boolean output rather than comparing to a value to determine result
    elif is_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")