
x=90
def myfnc(x):
    print('inside myfnc' ,x)
    x = 10
    print('inside myfnc' ,x)

x = 20
myfnc(x)
print(x)

def myfun(y):
    print('y= ',y)
    print('x=',x)


x = 20  # here x is a global variable
myfun(x)
#print('y= ',y) this can be happend cause y is a local variable