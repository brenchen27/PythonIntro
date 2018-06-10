import turtle

brendan=turtle.Turtle()

brendan.shape("turtle")
brendan.color("blue")
brendan.fillcolor("lime")

brendan.speed(10)

for i in range(5):
    brendan.forward(100)
    brendan.right(145)

turtle.exitonclick()
