# Example using replace() method
s = "hello world"
new_s = s.replace("world", "python")
print(new_s)  # Output: "hello python"

# Example using find() method
s = "hello world"
index = s.find("world")
print(index)  # Output: 6 (index of "world" within "hello world")

# If substring is not found, find() returns -1
index = s.find("python")
print(index)  # Output: -1 (since "python" is not found in "hello world")
