# 1 Positional Argument
def addition(a,b,c,d):
    sum=a+b+c+d
    print("The sum of All Positional Argument Number is :",sum)
addition(1,2,3,4,)

# 2 Default Argument
def addition(a,b,c,d=14):
    sum=a+b+c+d
    print("The sum of All Default Argument Number  is :",sum)
addition(1,2,3,)



# 3 Keyword Argument
def std_info(name,id,course):
     print('student Name is :',name)
     print('student Id Number is :',id)
     print('student Course is :',course)
     
std_info(course="MCA",name="Revan",id="GHRUA09")


#4 Varible length  Argument
  
def num(*arg):
      sum=0
      for s in arg:
          sum+=s
      print('The sum is :',sum)

num(1,2,3,4)

 
