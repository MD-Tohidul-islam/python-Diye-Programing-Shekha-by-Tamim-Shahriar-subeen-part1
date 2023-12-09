import turtle
def traingle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

traingle(100)
turtle.exitonclick()