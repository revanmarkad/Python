def factorial(n):
    if n==0:
        return 1
    else:
        f=n*factorial(n-1)
        return f
    
   
n=int(input("Enter Your Number :"))
x=factorial(n)
print("Given Number Factorial is :",x)