from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# ----------------------------------------------------------------------------------------
def next_card():
    pass 






# ----------------------------------------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_font_img = PhotoImage(file='/Users/computer/Desktop/100_days_of_python_pledge/Day31/flash-card-project-start/images/card_front.png')
canvas.create_image(400, 263, image=card_font_img)

canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file='/Users/computer/Desktop/100_days_of_python_pledge/Day31/flash-card-project-start/images/wrong.png')
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file='/Users/computer/Desktop/100_days_of_python_pledge/Day31/flash-card-project-start/images/right.png')
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

window.mainloop()