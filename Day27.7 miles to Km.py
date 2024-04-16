from tkinter import *


def miles_to_km():
    miles = float(text.get())
    kilometers = miles * 1.60934
    my_label3.config(text=f"{kilometers}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=200, width=400)
window.config(padx=50, pady=50)

text = Entry(width=10)
text.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Courier", 18))
my_label.grid(column=2, row=0)

my_label2 = Label(text="is equal to", font=("Courier", 18))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Courier", 18))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km", font=("Courier", 18))
my_label4.grid(column=2, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)


window.mainloop()
