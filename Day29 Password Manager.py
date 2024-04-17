from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_text_box.get()
    email = email_text_box.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(
        title="Verification",
        message=f"Would you like to save?\nEmail: {email}\nPassword: {password}",
    )
    if is_ok:
        with open("Password_Manager_data.txt", mode="a") as file:
            file.writelines(f"{website} | {email} | {password}\n")
        website_text_box.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="Password_Manager_img.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website entry section
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_text_box = Entry(width=20)
website_text_box.focus()
website_text_box.grid(column=1, row=1, columnspan=2, sticky="WE")

# Email/Username section
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
email_text_box = Entry(width=20)
email_text_box.insert(0, "xyz@gmail.com")
email_text_box.grid(column=1, row=2, columnspan=2, sticky="WE")

# Password section
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")
generate_button = Button(text="Generate Password", bg="#FEC7B4")
generate_button.grid(column=2, row=3)
# add Button
add_button = Button(
    text="Add", width=20, justify="left", bg="#5BBCFF", command=add_to_file
)
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")

window.mainloop()
