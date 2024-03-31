from turtle import Turtle, Screen

timmy = Turtle() # here timmy is object and Turtle is class used as blueprint
print(timmy)

my_screen=Screen()      # screen module shows the screen where or turtle will show
print(my_screen.canvwidth)
timmy.shape("turtle")
timmy.color("red","green")
timmy.forward(100)


my_screen.exitonclick()  #allows the popup screen to close onclick

