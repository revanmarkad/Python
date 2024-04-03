# Question:
# Take two inputs from the user, where the first is any word and the second is a single character separated by a comma.
# Print the length of the word and the number of times the given character is present in the word,
# considering case insensitivity.

name, char = input('Enter a word and a character separated by a comma: ').split(',')

 
char2 = char.lower()

 
name2 = name.lower()

 
print("Length of the original word:", len(name))

# Print the number of occurrences of the character in the word (case-insensitive)
print("Number of occurrences of the character in the word (case-insensitive):", name2.count(char2))
