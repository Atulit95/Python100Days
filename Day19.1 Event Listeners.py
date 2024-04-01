from turtle import Turtle, Screen

shin = Turtle()
screen = Screen()


def forward():
    shin.fd(10)


def backward():
    shin.backward(10)


def clockwise():
    shin.right(10)


def counter_clockwise():
    shin.left(10)


def clear():
    shin.clear()
    shin.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
