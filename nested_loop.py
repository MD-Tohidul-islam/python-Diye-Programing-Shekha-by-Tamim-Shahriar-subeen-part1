import turtle
turtle.Screen()
turtle.speed()
for i in range(50,100,10):
    for j in range(4):
        turtle.forward(i)
        turtle.left(90)
turtle.exitonclick()