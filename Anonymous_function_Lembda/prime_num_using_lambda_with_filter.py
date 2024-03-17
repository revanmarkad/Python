def prime_no(n):
    i=2
    f=0
    while(i<n):
        if(n%i==0):
            f=1
        i=i+1
    if(f==0):
        return True
    else:
        return False        
    
myList=[2,3,4,5,6,7,8,9]
ans=list(filter(prime_no,myList))
print(ans)