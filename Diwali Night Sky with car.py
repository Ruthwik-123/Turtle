import turtle as t
import random
import turtle
t.speed(0)
t.Screen().bgcolor('black')
t.setup(1000,800)
t.color('black')
t.up()
t.backward(500)
t.right(90)
t.forward(400)
t.left(90)
t.down()
t.begin_fill()
t.color('#1d557d') #037a8a #fireword bg color
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(800)
    t.left(90)
t.end_fill()

t.up()
t.left(90)
t.forward(450)
t.right(90)
t.down()

t.begin_fill()
t.color('#036194')  #water color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(450)
    t.right(90)
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.left(90)
t.down()

t.width(5)
t.color('silver') # bride color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(100)
    t.right(90)


for i in range(25):
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.right(90)

t.up()
t.right(90)
t.forward(105)
t.right(90)
t.down()

t.begin_fill()
t.color('black') #075419 #b38b4b #gross color
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.left(90)
t.forward(150)
t.down()

t.width(1)
t.begin_fill()  #Boat
t.color('black','#806608')
t.forward(50)
t.right(45)
t.forward(50)
t.right(135)
t.forward(120)
t.right(180)
t.right(-45)
t.forward(50)
t.right(45)
t.end_fill()

t.up()
t.forward(600)
t.right(90)
t.forward(85)
t.left(90)
t.down()

t.begin_fill()  #2Boat
t.color('black','#524f24')
t.forward(40)
t.right(45)
t.forward(30)
t.right(135)
t.forward(80)
t.right(180)
t.right(-45)
t.forward(30)
t.right(45)
t.end_fill()
t.up()
t.right(10)
t.goto(-400,370)
t.down()
t.left(180)
t.begin_fill()
t.color('black','white')
#t.right(30)
t.shape()
t.right(90)
t.circle(50,180)
t.backward(10)
t.left(180)
t.circle(-50,175)
t.forward(15)
t.end_fill()
#t.hideturtle()
t.setheading(0)
t.up()
t.forward(50)
t.down()


for i in range(5):
    colors = ['red','blue','white','green','yellow']
    chices = random.choice(colors)
    t.begin_fill()
    t.color(chices)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.end_fill()
    t.up()
    t.forward(200)
    t.setheading(0)
    t.down()

t.up()
t.home()
t.down()
t.hideturtle()

firework= t.Turtle()
firework.speed(0)
firework.begin_fill()
for i in range(0,1000,100):
    firework.color(random.choice(["#f70f07", "orange", "yellow", "#40f224", "#070ff7", "#fa05ac",'#f79f07','#abf707','#07f78b']))
    firework.up()
    firework.goto(440-i, random.randint(120, 380))
    firework.down()
    for _ in range(36):
        firework.forward(20)
        firework.backward(20)
        firework.left(10)
        firework.end_fill()
        firework.hideturtle()

car = t.Turtle()
car.up()
car.goto(-500,-330)
car.down()

# Drawing the white lines
car.color('white')
car.width(2)
for i in range(5):
    car.forward(100)
    car.up()
    car.forward(100)
    car.down()
car.up()
car.color('white')
car.goto(-500,-300)
#here you have rrr.gif this is what I downloaded, you can download another car image and paste its name here in the line 209.
a = turtle.Screen()
a.addshape('rrr.gif')
car.shape('rrr.gif')
for i in range(100):

    speed = 7.5  #speed of the moving car
    run = True
    while run:
        car.forward(speed)
        if car.xcor() > 500:
            car.hideturtle()
            car.goto(-500, -300)
            car.showturtle()
car.hideturtle()
run = False
car.down()
