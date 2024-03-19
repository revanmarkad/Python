import numpy as np
# 1 Reference ..................
# Reference can change both own memory or Reference memory 
arr=np.arange(1,11,1)
print(arr)

new_arr=arr
print("Reference",new_arr)

print("After change")
new_arr[3]=422
print(arr)

# 2 view

print(" In view")
arr_view=arr.view()
arr_view[1]=111 # changes is applicable are both arrays but memory location or id is diffrent
print(arr_view ,'view')
 
# 3 copy
print('copy')
arr_copy=arr.copy()

print(arr_copy,"copy")
arr[1]=00 #changes is not applicable in  copy it change only in arr . also both id`s  diffrent
print(arr_copy)
print(arr)