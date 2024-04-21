from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ------------------------------- FLASH CARD FRON DISPLAY-------------------#
try:
    data = pandas.read_csv("flashcard_save.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("FlashCard_french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def is_known():
    to_learn.remove(current_card)
    generate_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("flashcard_save.csv", index=FALSE)


# ------------------------------ UI DESIGN ---------------------------------#
window = Tk()
window.title("Flash Card Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="FlashCard_images\card_front.png")
back_img = PhotoImage(file="FlashCard_images\card_back.png")
card_background = canvas.create_image(400, 275, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Aerial", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Aerial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="FlashCard_images\wrong.png")
cross_button = Button(
    image=cross_img, border=0, highlightthickness=0, command=generate_word
)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file="FlashCard_images\check.png")
check_button = Button(image=check_img, border=0, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

generate_word()

window.mainloop()
