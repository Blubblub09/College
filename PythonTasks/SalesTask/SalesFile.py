#Asks for target file name
name = input("Enter File Name: ")

#Reads file contents and saves to content variable
with open(name, "r") as file:
    content = file.readlines()



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


# Defining the results
result = f"Number of lines: {len(content)} \nTotal number of characters: {sum(len(line) for line in content)} \nSmallest sale line: {smallest} \nLargest sale line: {largest}"

print(result)

#Asking if the user wants to save the results to a seperate file
choice = bool(input("Do you want to save the results to a new file? \n"
                    "1) Yes \n"
                    "0) No \n"))
if choice == 1:
    with open("results.txt", "w") as results:
        results.write(result)