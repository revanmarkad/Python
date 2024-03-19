import numpy as np

arr1=np.array([21,5,4,3,88,6,9],int)
arr2=np.array([1,5,4,93,88,68,9],int)

arr3=(arr1==arr2)

if(all(arr3)):
    print("Both Arrays having same element !!!!!!!")
else:
    print(" Arrays elements are diffrent not same !!!!!!!!")


if(any(arr3)):
    print("Both Arrays having same element (any)!!!!!!!")
else:
    print(" Arrays elements are diffrent not same (any) !!!!!!!!")
    
    
newarr=np.where(arr1%2==0,arr1,0)
print(newarr)