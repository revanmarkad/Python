def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


# Example usage:
input_string = input("Enter string:")
result = count_vowels(input_string)
print("Number of vowels:", result)
