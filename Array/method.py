# 1 append............................
import array as arr

# myArray=arr.array("i",[])
# n=int(input("Enter your array limit: "))
# print("Enter your Element :")
# for i in range(n):
#     x=int(input())
#     myArray.append(x)
# # print(myArray)




# 2 insert...................

myArray1=arr.array("i",[1,2,3,5,6,7])
myArray1.insert(3,4)
print(myArray1)


# 3 reverse...........................

myArray1.reverse()
print(myArray1)


# 4 count .................................

c=myArray1.count(7)
print(c)
