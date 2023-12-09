import turtle
turtle.Screen()
turtle.speed()
for i in range(4):
    for i in range(50,100,10):
        turtle.forward(i)
        turtle.left(90)
        turtle.forward(i)
        turtle.left(90)
turtle.exitonclick()
