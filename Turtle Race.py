import turtle
from turtle import Turtle
from random import randint

# Setting up the screen
turtle.setup(600, 400)
turtle.bgcolor('saddle brown')

# Drawing the finish line
turtle.up()
turtle.goto(200, 200)
turtle.down()
turtle.color('white', 'black')
for i in range(10):
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.up()
    turtle.backward(40)
    turtle.right(90)
    turtle.down()
    turtle.end_fill()
turtle.up()
turtle.home()
turtle.hideturtle()

# Adding turtles
blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5) #New concept
blue_turtle.penup()
blue_turtle.goto(-285, 150)
blue_turtle.pendown()

red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5) #New concept
red_turtle.penup()
red_turtle.goto(-285, 50)
red_turtle.pendown()

yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5) #New concept
yellow_turtle.penup()
yellow_turtle.goto(-285, -50)
yellow_turtle.pendown()

white_turtle = Turtle()
white_turtle.color("white")
white_turtle.shape("turtle")
white_turtle.shapesize(1.5) #New concept
white_turtle.penup()
white_turtle.goto(-285, -150)
white_turtle.pendown()

# Racing logic
race_on = True
while race_on:
    blue_turtle.forward(randint(1, 10))
    red_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))
    white_turtle.forward(randint(1, 10))

    if blue_turtle.xcor() >= 200:
        print('t1 wins')
        blue_turtle.shapesize(2.5)
        turtle.write('Blue turtle wins', font=('Arial', 20, 'bold'), align='center')
        race_on = False

    elif red_turtle.xcor() >= 200:
        print('t2 wins')
        red_turtle.shapesize(2.5)
        turtle.write('Red turtle wins', font=('Arial', 20, 'bold'), align='center')
        race_on = False

    if yellow_turtle.xcor() >= 200:
        print('t3 wins')
        yellow_turtle.shapesize(2.5)
        turtle.write('Blue turtle wins', font=('Arial', 20, 'bold'), align='center')
        race_on = False

    elif white_turtle.xcor() >= 200:
        print('t4 wins')
        white_turtle.shapesize(2.5)
        turtle.write('Red turtle wins', font=('Arial', 20, 'bold'), align='center')
        race_on = False




turtle.done()