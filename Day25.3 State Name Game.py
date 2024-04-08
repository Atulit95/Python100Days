IMAGE = "blank_states_img.gif"
import turtle

screen = turtle.Screen()
screen.title("State Name Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

answer_state = screen.textinput(title="State name", prompt="Enter the State name: ")

screen.exitonclick()
