import random
import string

code = input("Enter Your Srcret Code : ")
length = len(code)

if length > 3:
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    newCode = random_chars + code[1:] + code[0] + random_chars
    print("Your Code is:", newCode)


# decoding

if length < 3:
    print(code[::-1])
else:
    print("Decoded code is:", code)
