# def cube(x):
#     return x*x*x


# l=[1,2,3,4,5,6]
# newl=[]
# for item in l:
#     newl.append(cube(item))

# print(newl)

# # map


# def cube(x):
#     return x * x * x


# l = [1, 2, 3, 4, 5, 6, 7]

# newl = list(map(cube, l))
# print(newl)


# # filter
# l = [1, 2, 3, 4, 5, 6]


# def filter_function(a):
#     return a > 1


# newl = list(filter(filter_function, l))

# print(newl)




#Reduce

from functools import reduce

from numpy import number

Numbers=[1,2,3,4,5,6,7,8,9,10]


sum=reduce(lambda x,y:x+y,Numbers)

print(sum)
