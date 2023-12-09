def myfunc(y=10):
    print('y = ',y)


x = 20
myfunc(x)
myfunc()  # here y work as like a default parameter
print()
#def  myfn1 (x, y = 10, z): this is error
def myfn1(x,y = 10, z =2):
    print('x = ',x ,'y = ',y ,'z = ',z)

x = 5
y = 6
z = 7
myfn1(x,y,z)
print()
def myfn2(x,z,y = 10,):
    print('x = ',x ,'y = ',y ,'z = ',z)

x = 5
y = 6
z = 7
myfn2(x,y,z) # function follows the postion of argument

