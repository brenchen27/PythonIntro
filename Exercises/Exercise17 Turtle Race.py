import turtle
import random

##roboy
roboy=turtle.Turtle()
roboy.shape("turtle")
roboy.color("blue")
roboy.fillcolor("blue")
roboy.speed(100)

##ali-a
alia=turtle.Turtle()
alia.shape("turtle")
alia.color("red")
alia.fillcolor("red")
alia.speed(100)
alia.goto(-100,0)

##pabo
pabo=turtle.Turtle()
pabo.shape("turtle")
pabo.color("springgreen")
pabo.fillcolor("springgreen")
pabo.speed(100)
pabo.goto(-200, 0)



roboy.left(90)
roboy.write(roboy.position())

alia.left(90)
alia.write(alia.position())

pabo.left(90)
pabo.write(pabo.position())

foundWinner=False

for i in range(100):
    steps=random.randint(1,5)
    roboy.forward(steps)
    steps=random.randint(1,5)
    alia.forward(steps)
    steps=random.randint(1,5)
    pabo.forward(steps)


roboy.write(roboy.position())
alia.write(alia.position())
pabo.write(pabo.position())

turtle.exitonclick()
