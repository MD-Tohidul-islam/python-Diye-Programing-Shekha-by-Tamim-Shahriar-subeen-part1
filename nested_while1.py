import turtle
height = 5
width = 5
turtle.speed(5)
turtle.penup()
for y in range(height):
    for x in range(width):
        turtle.dot('blue')
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()