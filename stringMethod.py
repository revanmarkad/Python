# strings are immutable


data = "dambo @@@@@@@@@ @@@@@@@@@@@@@@@@@ @"
print(len(data))

print(data.upper())
print(data.lower())


print(
    data.rstrip("@")
)  # rstrip method to remove trailing "@" characters from the string. That's correct!     Just keep in mind that rstrip only removes characters from the end of the string. If you have "@" characters   in the middle or at the beginning, they won't be removed.


print(
    data.replace("dambo", "valtas")
)  # line is using the replace method to replace the substring "dambo" with "valtas" in the data string. If the substring "dambo" is present in data, it will be replaced, and the result will be printed.


print(
    data.split(" ")
)  # The split method is used to split a string into a list of substrings based on a specified delimiter. In your case, you are using a space (" ") as the delimiter.
# ans= ['dambo', '@@@@@@@@@', '@@@@@@@@@@@@@@@@@', '@']


heading = "in the journey of life, every challenge is an opportunity for growth. Embrace the obstacles, for they are the stepping stones to success."

print(
    heading.capitalize()
)  # capitalize method to capitalize the first letter of the string

heading2 = "in the journey of life, every challenge"
print(
    heading2.center(100)
)  # The center method is used to center-align a string within a specified width. In your case, you're centering the string heading2 within a width of 100 characters.


print("the count is:", heading2.count("l"))


print(
    heading2.endswith("revan")
)  # The endswith method is used to check if a string ends with a specified suffix.
print(heading2.endswith("challenge"))
# This means that "in the journey of life, every challenge" does not end with "revan," but it does end with "challenge."


names = "revan markad madhi pathardi"

print(
    "the ans is :", names.endswith("p", 0, 20)
)  # You are using the endswith method to check if the substring from index 0 to 19 (exclusive) of the names string ends with the character "p." The substring in this range is "revan markad madhi p," and it indeed ends with "p."  Therefore, the output of this code will be: true


print(
    names.find("m")
)  # You are finding the index of the first occurrence of the letter "m" in the names string. The result will be the index of the first "m" found in the string.
# In this case, "m" first appears in the string at index 6 (0-based indexing), so the output will be:6


print(
    # names.index("mooo")
)  # The substring "mooo" is not present in the names string. Therefore, running this code will result in a ValueError. If you want to avoid the error, you might want to check if the substring exists before using index.


print(
    names.isalnum()
)  # The string names contains spaces and is not composed solely of alphanumeric characters, so the output will be False. If you want to check if all characters are alphanumeric excluding spaces, you might want to remove spaces before using isalnum:


print(
    names.title()
)  # This will capitalize the first letter of each word in the names string, resulting in the output:Revan Markad Madhi Pathardi
