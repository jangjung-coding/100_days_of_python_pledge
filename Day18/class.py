from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# for _ in range(4): # Make a square
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# for _ in range(15): # Draw a dashed line
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
turtle_colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "brown", "cyan"]

# for number_of_sides in range(3, 11):
#     angle = 360 / number_of_sides
#     random_color = random.choice(turtle_colors)
#     timmy_the_turtle.color(random_color)
    
#     for _ in range(number_of_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# Draw a random walk
# directions = [0, 90, 180, 270]

# for _ in range(200):
#     timmy_the_turtle.forward(random.randint(10, 50))
#     timmy_the_turtle.setheading(random.choice(directions))

# Draw a spirograph
timmy_the_turtle.speed("fast")
for _ in range(72):
    timmy_the_turtle.color(random.choice(turtle_colors))
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 5)

screen = Screen()
screen.exitonclick()