#  "Counting Lists Within a List".

def find(l):
    
    count=0
    for i in range(len(l)):
        
        if type(l[i])==list:
            count+=1
    return count   
         
         
     
    
print(find([1,2,3,[4,5,6],1,2,3,[4,5,6],1,2,3,[4,5,6]]))