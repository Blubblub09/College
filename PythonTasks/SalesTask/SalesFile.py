#Asks for target file name
name = input("Enter File Name: ")

#Reads file contents and saves to content variable
with open(name, "r") as file:
    content = file.readlines()

#Determines the length of the file and the amount of lines
print("Number of lines:", len(content) ,"\n"
      #Adds the length of every item in the list
      "Total number of characters:", sum(len(line) for line in content))

high = -1
low = -1

#Determines if number is the new highest or lowest
for item in content:
    if item[-1]=="\n":
        num = int(item[-2])
    else:
        num = int(item[-1])
    
    if num > high or high == -1:
        largest = item
        high = num
    
    if num < low or low == -1:
        smallest = item
        low = num

print("Smallest sale line:", smallest ,"\n"
      "Largest sale line:", largest)