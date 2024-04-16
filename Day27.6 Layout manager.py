from tkinter import *


def change_label():
    my_label.config(text="I am A new Label")


window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # to add the padding


# Label
my_label = Label(text="I am a Label", font=("Algerian", 24))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)


# Button
button1 = Button(text="Here! Click Me.", command=change_label)
button2 = Button(text="No! Click Me.", command=change_label)
# button.pack()
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)
button1.config(padx=20, pady=20)  # to add the padding

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
