# wrrite a programe which make like this bangladesh = abgndaseh
v = 'bangladesh'
v = input('enter a string: ')
b = ""
for i in range(0,len(v),2):
    b+=v[i:i+2][::-1]
print(b)