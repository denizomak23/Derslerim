import turtle
import random

t = turtle.Turtle()

for x in range(10):
    I=list(range(10))
    I=["red","blue","green","yellow","black","white","pink","orange","purple","brown"]
    t.color(random.choice(I))   
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    ku = random.randint(1, 100)  
    t.forward(300)
    t.right(30)

turtle.done()