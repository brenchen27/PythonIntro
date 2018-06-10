import turtle

t=turtle.Turtle()
t.speed(10)

turtle.bgcolor("blue")

def createRec(x,y,width,height,color):
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.penup()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.left(90)

def createStar(x,y,length,color):
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.penup()
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

def createCircle(x,y,size,color):
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.penup()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

for i in range(20):
    startingX = -100+5*i
    startingY = 20+10*i
    width=200-10*i
    createRec(startingX,startingY,width,10,"green")



createRec(-10,-20,20,40,"brown")
createStar(-20,230,40,"gold")
createCircle(200,200,60,"white")
createCircle(190,200,60,"blue")
turtle.exitonclick()
