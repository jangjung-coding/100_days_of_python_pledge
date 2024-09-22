from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100 
for i in range(6):    
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y_position)
    y_position += 40
    
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color. ")
print(f"You have bet on {user_bet} turtle")

screen.exitonclick()