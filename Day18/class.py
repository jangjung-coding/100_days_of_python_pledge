from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# for _ in range(4): # Make a square
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for _ in range(15): # Draw a dashed line
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


screen = Screen()
screen.exitonclick()