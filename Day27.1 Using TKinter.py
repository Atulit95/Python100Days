import tkinter

window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label", font=("Courier", 24, "italic", "bold"))

my_label.pack(side="left")

window.mainloop()
