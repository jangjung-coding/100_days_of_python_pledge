import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\samsung\Desktop\100_days_of_python_pledge\Day25\us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv(r"C:\Users\samsung\Desktop\100_days_of_python_pledge\Day25\us-states-game-start\us-states-game-start\50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", 
                                prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())   
    
screen.exitonclick()