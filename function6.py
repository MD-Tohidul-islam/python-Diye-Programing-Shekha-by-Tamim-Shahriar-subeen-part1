def add_num(l):
    result = 0
    for i in l:
        result+=i
    return result

v = list(range(10))
print(v)
result = add_num(v)
print(result)
print(v)
print()
def test_fn(li):
    li[0] = 10
    b=sum(li)
    return b

my_list = [1,2,3,4,5,6]
print('before function call',my_list)
b = test_fn(my_list)
print(b)
print('after function call',my_list)
def average(l):
    return sum(l)/len(l)

def aver(l):
    total = 0
    for i in l:
           total+=i
    return total/len(l)
my_list = [1,2,3,4,5,6]
ave= average(my_list)
print(aver(my_list))
print(ave)