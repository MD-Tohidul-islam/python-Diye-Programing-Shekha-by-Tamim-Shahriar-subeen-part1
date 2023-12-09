n= 23
n1 = 34
n2 =83
if n>n1:
    max_n = n
else:
    max_n = n1
if n2>max_n:
    max_n = n2
print(max_n)
if n> n1 and n>n2:
    big = n
elif n1>n and n1>n2:
    big = n1
else:
    big = n2
print(big)