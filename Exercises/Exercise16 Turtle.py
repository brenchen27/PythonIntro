import turtle

brendan = turtle.Turtle()

brendan.shape("turtle")
brendan.color("blue")
brendan.fillcolor("lime")

brendan.speed(100)

for i in range(180):
    brendan.forward(100)
    brendan.right(30)
    brendan.forward(20)
    brendan.left(60)
    brendan.forward(50)
    brendan.right(30)

    brendan.penup()
    brendan.setposition(0, 0)
    brendan.pendown()

    brendan.right(2)



turtle.exitonclick()
