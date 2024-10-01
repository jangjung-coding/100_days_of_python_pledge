import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\samsung\Desktop\100_days_of_python_pledge\Day25\us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", 
                                prompt="What's another state's name?")
print(answer_state)

