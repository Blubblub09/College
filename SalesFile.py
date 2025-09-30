#Asks for target file name
name = input("Enter File Name: ")

#Reads file contents and saves to content variable
with open(name, "r") as file:
    content = file.read()

    print("Number of lines:", len(file.readlines()) ,"\n"
          "Total number of characters:", len(content) ,"\n"
          "Shortest sale line:", 3 ,"\n"
          "Largest sale line:", 3 ,"\n")

