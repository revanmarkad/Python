r=int(input("Enter the value of r:"))

match r:
    case 0:
        print('r is zero')

    case 3:
        print('r is 3')

    case _ if r==22:
        print(r,"is 22")
        
    case _:
        print(r)