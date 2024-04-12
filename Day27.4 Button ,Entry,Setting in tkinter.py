from tkinter import *

window = Tk()
window.title("Button")
window.minsize(width=500, height=500)

my_label = Label(text="I am a Label", font=("Algerian", 24))
my_label.pack()

# Button

# Change label text to any new text on click of a button


def change_label():
    my_label.config(text="I am A new Label")


button = Button(text="Here! Click Me.", command=change_label)
button.pack()


window.mainloop()
