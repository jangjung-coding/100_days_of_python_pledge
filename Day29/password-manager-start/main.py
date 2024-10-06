# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk

window = tk.Tk() # create a window
window.title("Password Manager") # set the title of the window
window.config(padx=50, pady=50) # set the padding of the window

canvas = tk.Canvas(width=200, height=200) # create a canvas
logo_img = tk.PhotoImage(file="logo.png") # load the image
canvas.create_image(100, 100, image=logo_img) # create the image
canvas.grid(column=1, row=0) # set the position of the canvas

# Labels
website_label = tk.Label(text="Website:") # create a label
website_label.grid(column=0, row=1) # set the position of the label

email_label = tk.Label(text="Email/Username:") # create a label
email_label.grid(column=0, row=2) # set the position of the label

password_label = tk.Label(text="Password:") # create a label
password_label.grid(column=0, row=3) # set the position of the label

# Entries
website_entry = tk.Entry(width=35) # create an entry
website_entry.grid(column=1, row=1, columnspan=2) # set the position of the entry
website_entry.focus() # set the focus on the entry

email_entry = tk.Entry(width=35) # create an entry
email_entry.grid(column=1, row=2, columnspan=2) # set the position of the entry
email_entry.insert(0, "jangisalive1650@gmail.com") # set the default value of the entry

password_entry = tk.Entry(width=18) # create an entry
password_entry.grid(column=1, row=3) # set the position of the entry

# Buttons
generate_password_button = tk.Button(text="Generate Password") # create a button
generate_password_button.grid(column=2, row=3) # set the position of the button

add_button = tk.Button(text="Add", width=33) # create a button
add_button.grid(column=1, row=4, columnspan=2) # set the position of the button

window.mainloop() # keep the window open