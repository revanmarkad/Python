import array as arr

myarr=arr.array('i',[])

n=int(input("Enter your range of array :"))

for i in range(n):
    x=int(input("Enter your Element :"))
    myarr.append(x)
    
for i in range(n):
    print(myarr[i],end=" ")
    