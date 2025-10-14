'''
WEEK 03 Exercise - Application of recent learning
Incorporate your recent studies of Python data structures and file handling to solve the following, e.g. 
- file handling and methods
- strings
- lists
- sets and/or dictionaries

along with the relevant functions/methods they offer.

Paul Knighton
'''
# Open a word_list.txt file for reading
with open("PythonTasks/Week 6/InputValidation/words.txt", "r") as file:
# Main file reading loop:
    all_lines = []
    for line in file:
        # read all lines into a list 
        all_lines.append(line.strip().lower())
# count the number of lines in a file
line_count = len(all_lines)

# Main processing of list:
# print all items in the list
print(all_lines)

# print the number of items in the list
print(line_count)

# print all items in the list in alphabetic order A-Z (ascending), e.g. sorted.
all_lines.sort()
print(all_lines)

# print all items in the list in alphabetic order Z-A (descending), eg sorted and reversed.
all_lines.sort(reverse = True)
print(all_lines)

# print the shortest word and its' length
all_lines.sort(key = len)
print(f"{all_lines[0]} is the shortest word with a length of {len(all_lines[0])}")

# print the longest word and its' length
all_lines.sort(key = len, reverse = True)
print(f"{all_lines[0]} is the longest word with a length of {len(all_lines[0])}")

# print number of items in the list, the first item and the last item of list.
print(f"There are {len(all_lines)} in the list, first={all_lines[0]}, last={all_lines[-1]}")

# print only the unique items in the list, along with the number of times each one occurs in the list

unique_items = {}
for word in all_lines:
    if word in unique_items:
        unique_items[word] = unique_items[word] + 1
    else:
        unique_items[word] = 1
print(unique_items)

# print the number of unique items in the list
print(len(unique_items))

# Scrabble / Word finder v1:
# in a loop ask the user for a start letter,
# then print all words beginning with a specific letter, which the user inputs.
# e.g. "a"
# andes
# apple
# avalanche
letter = input(f"Enter a starting letter: ")

items = [item for item in all_lines if item[0] == letter]
print(items)

# Scrabble / Word finder v2:
# Extend your Scrabble / Word finder to print all words beginning with a specific letter, which are a specific number of letters long, which the user inputs.
# e.g. inputs of "e" and "6" would find.
# echoes
letter = input(f"Enter a starting letter: ")
length = int(input(f"Enter the length of the words: "))

items = [item for item in all_lines if item[0] == letter and len(item) == length]
print(items)

# Finding possible words with partial letters given
possible = all_lines
given_letters = input("Input letters of a word, insert '?' in place of unknown letters (e.g. 'a??in?' = 'acting') \n").lower()

for position in range(len(given_letters)):
    if given_letters[position] != "?":
        possible = [word for word in possible if word[position] == given_letters[position] and len(word) == len(given_letters)]

print(f"Possible words:\n {possible}")

from fnmatch import filter
possible = filter(all_lines, given_letters)
print(f"Possible words:\n {possible}")
