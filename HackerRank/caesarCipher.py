# Function to encrypt a string using the Caesar Cipher with a given rotation factor
def caesarCipher(s, k):
    """
    Encrypts a string using the Caesar Cipher with a rotation factor.

    Args:
        s (str): The string to be encrypted.
        k (int): The rotation factor.

    Returns:
        str: The encrypted string.
    """
    # Initialize an empty string to store the encrypted message
    encrypted = ''
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is a lowercase letter
        if char.islower():
            # Calculate the new position of the character after rotation
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        # Check if the character is an uppercase letter
        elif char.isupper():
            # Calculate the new position of the character after rotation
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            # If the character is not a letter, leave it unchanged
            new_char = char
        # Append the new character to the encrypted message
        encrypted += new_char
    
    # Return the encrypted message
    return encrypted

# Example usage
s = "middle-Outz"
k = 2
result = caesarCipher(s, k)
print(result)  # Output: okffng-Qwvb
