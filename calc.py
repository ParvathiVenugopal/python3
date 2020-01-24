import calcmodule as c
a=int(input("enter a number"))
b=int(input("enter a number"))
o=input("enter the operation:")
if(o=='+'):
    print(c.add(a,b))
elif(o=='-'):
    print(c.subtract(a,b))
elif(o=='*'):
    print(c.mult(a,b))
else:
    print(c.div(a,b))