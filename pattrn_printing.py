# Q1 print following type of pattrn
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
 
length=int(input("Enter your length: "))
for i in range(1,length+1,1):
    for j in range(1,i+1,1):
        print('*',end=" ")
    print()




# Q2 print following type of pattrn
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


length=int(input("Enter your length: "))
for i in range(1,length+1,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
    
# Q3 print following type of pattrn
    
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
length=int(input("Enter your length: "))
for i in range(1,length+1,1):
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()