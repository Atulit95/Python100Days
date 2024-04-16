from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    Short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        count_down(work_sec)
        timer_label.config(fg=GREEN, text="Work")
    elif reps == 7:
        count_down(long_break)
        timer_label.config(fg=RED, text="Long Break")
    else:
        count_down(Short_break)
        timer_label.config(fg=PINK, text="Short Break")
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(
    text="Timer", font=(FONT_NAME, 30, "bold"), background=YELLOW, foreground=GREEN
)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="pomodoro_timer_bg.png")
canvas.create_image(100, 120, image=tomato)
timer_text = canvas.create_text(
    100, 150, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white"
)
canvas.grid(column=1, row=1)


# Buttons
start_button = Button(
    text="Start",
    font=(FONT_NAME, 8, "bold"),
    bg="#FFE4CF",
    width=8,
    foreground="#8c52ff",
    border=0,
    activebackground="#D37676",
    command=start_timer,
)
start_button.grid(column=0, row=3)

reset_button = Button(
    text="Reset",
    font=(FONT_NAME, 8, "bold"),
    bg="#FFE4CF",
    width=8,
    foreground="#8c52ff",
    border=0,
    activebackground="#D37676",
    command=reset_timer,
)
reset_button.grid(column=2, row=3)


check_marks = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=4)

window.mainloop()
