import turtle
t = turtle.Turtle()
t.color("blue")
t.speed(100)
t.hideturtle()
t.goto(-500,0)
t.begin_fill()
t.goto(0,0)
t.forward(500)

for i in range(4):
    t.left(90)
    t.forward(1000000000)
t.end_fill()
t.forward(1000000000)
t.goto(0,0)


t.color('black','#8a5c01')
t.speed(100)
#t.hideturtle()
t.goto(-500,0)
t.begin_fill()
t.goto(0,0)
t.forward(500)

for i in range(4):
    t.right(90)
    t.forward(1000000000)
t.end_fill()
t.forward(1000000000)
t.goto(0,0)




t.penup()
t.goto(-25,-75)
t.pendown()
t.left(90)
t.width(5)
t.color('green') #line
t.forward(250)
t.left(90)

t.begin_fill()
t.color('red')  #flower color
for i in range(6):
    t.circle(100-i,90)
    t.left(90)
    t.circle(100-i,90)
    t.left(30)
t.end_fill()

t.penup()
t.right(90)
t.forward(20)
t.left(90)
t.pendown()
#t.forward(200)
t.begin_fill()
t.color('#f5e556') #inside flower yellow
t.circle(20)
t.end_fill()

t.penup()
t.left(90)
t.forward(200)
t.left(90)
t.pendown()

t.begin_fill()
t.color('green') #leaf color
t.left(90)
t.circle(50,90)
t.left(90)
t.circle(50,90)

t.penup()
t.right(90)
t.forward(55)
t.left(90)
t.pendown()


t.left(90)
t.circle(-40,90)
t.left(-90)
t.circle(-40,90)

t.end_fill()

turtle.done()