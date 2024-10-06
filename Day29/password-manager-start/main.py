import tkinter as tk
from tkinter import messagebox
import random
import pyperclip # copy to clipboard automatically

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    
    password = password_letters + password_symbols + password_numbers
    
    random.shuffle(password)
    
    password =  "".join(password)
    
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    
    if is_ok:
        with open("list.txt", "a") as list_file:
            list_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, tk.END) # clear the entry
            password_entry.delete(0, tk.END)
        
# ---------------------------- UI SETUP ------------------------------- #
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
generate_password_button = tk.Button(text="Generate Password", command=generate_password) # create a button
generate_password_button.grid(column=2, row=3) # set the position of the button

add_button = tk.Button(text="Add", width=33, command=save) # create a button
add_button.grid(column=1, row=4, columnspan=2) # set the position of the button

window.mainloop() # keep the window open