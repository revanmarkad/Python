a=0
b=1
def fibo(n):
    global a,b
    if n==0:
        return
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
        fibo(n-1)
        
n=int(input("Enter Your Number:"))
x=fibo(n)
# print("Given Number fiboonacci series is :",x)