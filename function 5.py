def fn(x,z,y = 10):
    print('x = ', x, 'y = ', y, 'z = ', z)

fn(x=1,y=2,z=5)
a = 5
b = 6
fn(x =a ,z = b)
a = 1
b = 2
c = 3
fn(y= a,z = b, x = c)
