 # Function 1: Count the number of vowels in the input string
def count_vowel(s):
    """
    Count the number of vowels (both lowercase and uppercase) in the input string.
    
    Args:
    - s (str): Input string
    
    Returns:
    - int: Count of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# Function 2: Count duplicate vowels and their occurrences in the input string
import numpy as np

def count_duplicate_vowels(user_input):
    """
    Count duplicate vowels and their occurrences in the input string.
    
    Args:
    - user_input (str): Input string
    
    Returns:
    - dict: Dictionary containing duplicate vowels and their counts
    """
    myArr = np.array(['a', 'e', 'i', 'o', 'u'])
    user_input = user_input.lower()
    vowel_counts = {vowel: 0 for vowel in myArr}
    
    # Count occurrences of each vowel in the input string
    for vowel in myArr:
        vowel_counts[vowel] = user_input.count(vowel)
    
    # Filter out vowels with counts greater than 1 (duplicates)
    duplicate_vowels = {vowel: count for vowel, count in vowel_counts.items() if count > 1}
    
    # Check if duplicate vowels were found
    if not duplicate_vowels:
        return "Duplicate vowels not found."
    else:
        return duplicate_vowels
    

# Function 3: Return the index of each vowel in the input string
def vowel_Index(user_input):
    """
    Return the index of each vowel in the input string.
    
    Args:
    - user_input (str): Input string
    
    Returns:
    - list: List of vowel-index pairs
    """
    user_input = user_input.lower()
    input_length = len(user_input)
    result = []
    
    # Iterate over each character in the input string
    for i in range(input_length):
        if user_input[i] in 'aeiou':
            # Append vowel-index pair to the result list
            result.append(user_input[i] + ":" + str(i))
    
    return result


# Function 4: Remove vowels from the input string
def Remove_Vowels(user_input):
    """
    Remove vowels from the input string.
    
    Args:
    - user_input (str): Input string
    
    Returns:
    - str: Modified string with vowels removed
    """
    user_input = user_input.lower()
    input_length = len(user_input)
    ans = ''
    
    # Iterate over each character in the input string
    for i in range(input_length):
        # Append non-vowel characters to the ans string
        if user_input[i] not in 'aeiou':
            ans += user_input[i]
    return ans
