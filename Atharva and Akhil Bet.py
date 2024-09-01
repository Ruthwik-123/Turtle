import turtle
turtle.bgcolor("black")
x = turtle.Turtle()
x.hideturtle()
x.speed(999999999999999999999999999)
x.penup()
x.goto(-635, 350)
x.pendown()
x.color("white")
x.speed(0.000000001)
y = turtle.Turtle()
y.hideturtle()
y.speed(999999999999999999999999999)
y.color("white")
y.penup()
y.goto(645,340)
y.pendown()
y.begin_fill()
y.circle(25)
y.end_fill()
for i in range(10):
    for i in range(100):
        x.begin_fill()
        for i in range(5):
            x.left(144)
            x.forward(50)
        for i in range(1):
            x.forward(10)

            for i in range(5):
                x.left(144)
                x.forward(50)
        x.end_fill()

    x.penup()
    x.right(90)
    x.forward(75)
    x.right(90)
    x.forward(1000)
    x.left(180)
    x.pendown()
turtle.done()