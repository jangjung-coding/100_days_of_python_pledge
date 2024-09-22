from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def turn_left():
    tim.seth(tim.heading() + 10)
    
def turn_right():
    tim.seth(tim.heading() - 10)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()