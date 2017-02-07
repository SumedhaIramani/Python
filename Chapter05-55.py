#Write a program to draw a chessboard


import turtle


turtle.showturtle()
turtle.color("Black")
turtle.setheading(315)
turtle.circle(170,steps=4)
turtle.home()


for y in range(0,240,60):
    for x in range(0,240,60):
        turtle.goto(x,y)
        turtle.setheading(315)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color("black")
        turtle.circle(21,steps=4)
        turtle.end_fill()
        turtle.penup()  
        

for y in range(30,240,60):
    for x in range(30,240,60):
        turtle.goto(x,y)
        turtle.setheading(315)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color("black")
        turtle.circle(21,steps=4)
        turtle.end_fill()
        turtle.penup() 

turtle.hideturtle()  
turtle.done()