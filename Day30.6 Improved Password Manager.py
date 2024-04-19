from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from random import *


def gerated_pass():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_entry.delete(0, END)
    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_char = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_char

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_text_box.get().lower()
    email = email_text_box.get()
    password = password_entry.get()
    json_data_dic = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        is_ok = False
        messagebox.showerror(title="Error", message="Please fill all the details.")
    else:
        is_ok = messagebox.askokcancel(
            title="Verification",
            message=f"Would you like to save?\nEmail: {email}\nPassword: {password}",
        )

        if is_ok:
            try:
                with open("Password_Manager_data.json", mode="r") as file:
                    data = json.load(file)
                    # print(type(data))

            except FileNotFoundError:
                with open("Password_Manager_data.json", mode="w") as file:
                    json.dump(json_data_dic, file, indent=4)
            else:
                data.update(json_data_dic)

                with open("Password_Manager_data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_text_box.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH SETUP ------------------------------- #
def search():
    website = website_text_box.get().lower()
    if website!="":
        try:
            with open("Password_Manager_data.json", mode="r") as file:
                data = json.load(file)
                # print(type(data))

        except FileNotFoundError:
            messagebox.showerror(title="Opps!", message="Data file not present.")

        else:
            if website in data:
                new_data = data[website]
                messagebox.showinfo(title=f"{website} details==>",message=f"Email: {new_data["email"]} \nPassword: {new_data["password"]}")
            else:
                messagebox.showerror(title="Opps!",message=f"{website} not in database.")
            website_text_box.delete(0,END)
    else:
        messagebox.showerror(title="Opps!",message=f"Please enter a website.")

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
website_text_box = Entry(width=30)
website_text_box.focus()
website_text_box.grid(column=1, row=1, sticky="W")
search_button = Button(text="Search", bg="#FEC7B4", command=search)
search_button.grid(row=1, column=2, sticky="WE")


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
generate_button = Button(text="Generate Password", bg="#FEC7B4", command=gerated_pass)
generate_button.grid(column=2, row=3)
# add Button
add_button = Button(
    text="Add", width=20, justify="left", bg="#5BBCFF", command=add_to_file
)
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")

window.mainloop()
