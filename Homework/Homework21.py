import turtle

brendan=turtle.Turtle()

brendan.shape("turtle")
brendan.color("blue")
brendan.fillcolor("lime")

brendan.speed(10)

brendan.penup()
brendan.setposition(-100, 0)
brendan.pendown()

brendan.left(180)
brendan.forward(50)
brendan.left(90)
brendan.forward(100)
brendan.left(90)
brendan.forward(50)

brendan.penup()
brendan.setposition(0, 0)
brendan.pendown()

brendan.left(180)
brendan.forward(50)
brendan.left(90)
brendan.forward(50)
brendan.left(90)
brendan.forward(50)
brendan.right(90)
brendan.forward(50)
brendan.right(90)
brendan.forward(50)

turtle.exitonclick()
