#Asks for teas and coffees sold
teas = int(input("How many teas? "))
coffees = int(input("How many coffees? "))

#Prints income
print("Total income is £"+str(teas*2 + coffees*3))
print("The average price of drink sold was £"+ str((teas*2 + coffees*3) / (teas+coffees)))