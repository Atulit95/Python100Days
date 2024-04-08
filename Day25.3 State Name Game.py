# Our goal is to create game which is simmilar to game in given link
# Link:- "https://www.sporcle.com/games/g/states"
import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("State Name Game")
screen.setup(width=725, height=491)

screen.addshape(IMAGE)
turtle.shape(IMAGE)
state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 State name", prompt="Enter the State name: "
    ).title()

    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_detail = state_data[state_data.state == answer_state]
        t.goto(int(state_detail.x), int(state_detail.y))
        t.write(answer_state)
    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        break

missed_state = pandas.DataFrame(missing_state)
missed_state.to_csv("missed_state.csv")


screen.exitonclick()
