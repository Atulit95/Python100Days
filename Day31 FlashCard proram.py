from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------- FLASH CARD FRON DISPLAY-------------------#
data = pandas.read_csv("FlashCard_french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def generate_word():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card["French"])


def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_card["English"])


# ------------------------------ UI DESIGN ---------------------------------#
window = Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="FlashCard images\card_front.png")
back_img = PhotoImage(file="FlashCard images\card_back.png")
card_front_img = canvas.create_image(400, 275, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Aerial", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Aerial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="FlashCard images\wrong.png")
cross_button = Button(
    image=cross_img, border=0, highlightthickness=0, command=generate_word
)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file="FlashCard images\check.png")
check_button = Button(
    image=check_img, border=0, highlightthickness=0, command=generate_word
)
check_button.grid(row=1, column=1)

generate_word()

window.mainloop()
