import turtle
def draw_square(side_lenght):
    for i in range(4):
        turtle.forward(side_lenght)
        turtle.left(90)


couter = 0
while couter < 90:
    draw_square(100)
    turtle.right(4)
    couter+=1
turtle.exitonclick()