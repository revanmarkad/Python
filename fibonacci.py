a = 0
b = 1
num = int(input("Enter a number to obtain fibonacci sequences:"))


if num == 1:
    print(a)
else:
    # print(a)
    # print(b)
    for i in range(0, num):
        c = a + b
        a = b
        b = c
        print(c)
