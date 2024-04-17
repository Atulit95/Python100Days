from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)
canvas = Canvas(width=300, height=200)
lock_img = PhotoImage(file="Password_Manager_img.png")
canvas.create_image(150, 100, image=lock_img)
canvas.pack()

# website entry section
website_label = Label(text="Website:")
website_label.pack()
website_text_box = Entry(width=50)
website_text_box.pack()

# Email/Username section
Email_label = Label(text="Email/Username:")
Email_label.pack()
email_text_box = Entry(width=50)
email_text_box.pack()

# Password section
password_label = Label(text="Password:")
password_label.pack()

generate_button = Button(text="Generate Password")

# add Button
add_button = Button(text="Add")
add_button.pack()

window.mainloop()
