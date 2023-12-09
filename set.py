a = {1,2,3,4,5}
b = {2,4,5,8}
c = a-b # element in a but not in b
x = b-a # element in b but not in a
l = a|b # union
l1 = b|a
n = a&b # intesection (common element)
n1 = b&a # intesection
m = a^b # elemennt any of them but not both of them
m1 = b^a #
print(c)
print(x)
print(l,'and ', l1)
print(n,'and ', n1)
print(m,'and ', m1)
