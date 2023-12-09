number = [4,5,644,3,4,55,42,5,677,345,635]
v = max(number)
print(v)
big_number = number[0]
for i in number:
    if i>big_number:
        big_number = i
print(big_number)
l = []
total = 0
for i in range(1,101):
    if i%5 == 0:
        l.append(i)
        total+=i

print(l)
print(total)
total1 =0
for i in range(5,101,5):
     print(i)
     total1+=i
print('sum is : ', total1)
import  turtle
turtle.speed(1)
for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
turtle.exitonclick()


