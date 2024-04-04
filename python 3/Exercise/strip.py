# Example string with leading and trailing characters
s = "   hello world   "

# Removing leading whitespace
stripped_left = s.lstrip()
print(stripped_left)  # Output: "hello world   "

# Removing trailing whitespace
stripped_right = s.rstrip()
print(stripped_right)  # Output: "   hello world"

# Removing both leading and trailing whitespace
stripped_both = s.strip()
print(stripped_both)  # Output: "hello world"

# Removing specific characters
s = "###hello world###"

# Removing leading #
stripped_left = s.lstrip("#")
print(stripped_left)  # Output: "hello world###"

# Removing trailing #
stripped_right = s.rstrip("#")
print(stripped_right)  # Output: "###hello world"

# Removing both leading and trailing #
stripped_both = s.strip("#")
print(stripped_both)  # Output: "hello world"

