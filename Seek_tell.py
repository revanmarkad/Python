with open("seek.txt", "r") as f:
    print(type(f))

    f.seek(10)

    print(f.tell)
    data = f.read(15)
    print(data)
