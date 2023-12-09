import turtle
import random
colors = ['red','green','blue','yellow','orange','black','purple']
turtle.penup()
for i in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.setposition(x,y)
    i = random.randint(0,len(colors)-1)
    turtle.dot(colors[i])
turtle.done()