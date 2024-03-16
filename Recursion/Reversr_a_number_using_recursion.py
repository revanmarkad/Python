s=0
def reverse(n):
    global s
    if n>0:
        r=n%10
        s=s*10+r
        n=n//10
        reverse(n)
    return s
        
        
n=int(input("Enter Your Number: "))
x=reverse(n)
print("Given Number Reversed is :",x)