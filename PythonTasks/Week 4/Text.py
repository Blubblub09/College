#Asks for book title
book = input("Enter the title of a book \n")

# Prints title info
print("The title has", len(book) ,"characters. \n"
"The title in uppercase:", str.upper(book))

book2 = input("Enter the title of another book \n")

if len(book) > len(book2):
    print("'"+ book +"' is a longer title than '"+ book2 +"'")
elif len(book) < len(book2):
    print("'"+ book2 +"' is a longer title than '"+ book +"'")
else:
    print("'"+ book +"' and '"+ book2 +"' are equal length")