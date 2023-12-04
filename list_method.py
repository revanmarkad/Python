list=[1,2,3,4,5,6,7,8,9]
print(list)

list.append(10) #using append we caan add values last of the array or list
print(list)

# 2
sorting=[1,0,4,3,7,6,5,]
sorting.sort() # sort sorting list by ascending order
sorting.sort(reverse=True) #sort(reverse=True) sorting list by descending order
print(sorting)

# 3

rev=[1,2,3,4,5,6]
rev.reverse() # reverse() gave us to reverse of list
print(rev.index(4)) # .index() return a index 
print(rev)


coun=[1,2,3,4,5,5,6,6,1,1,1,8,8,]

print(coun.count(1)) # .count(1) counting the valu how many time its comming...


ins=[7,543,234,765,4567,99]

ins.insert(1,464) # insert adding vaalue at any index we added 464 at 1st index 
print(ins)



newList=[12,34,56,78,90]
list.extend(newList) #.extend( ) add  whole list of the another list last position
print(list)