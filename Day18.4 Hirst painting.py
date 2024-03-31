# import colorgram

# colors = colorgram.extract("hirst_painting.jpeg", 66)
# rgb_list = []
# for rgb_color in range(0, 31):
#     fir = colors[rgb_color]
#     rgb = fir.rgb
#     rgb_list.append((rgb.r, rgb.g, rgb.b))

# print(rgb_list)
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (210, 150, 100),
    (178, 67, 37),
    (15, 24, 41),
    (239, 209, 94),
    (71, 30, 35),
    (231, 66, 38),
    (157, 26, 20),
    (85, 91, 113),
    (117, 33, 39),
    (141, 154, 165),
    (159, 141, 71),
    (65, 42, 36),
    (183, 85, 94),
    (162, 62, 67),
    (232, 173, 159),
    (50, 52, 126),
    (165, 140, 148),
    (99, 116, 115),
    (13, 23, 22),
    (178, 183, 181),
    (223, 174, 180),
    (127, 122, 141),
    (185, 187, 204),
    (74, 71, 48),
    (187, 194, 190),
    (112, 139, 142),
    (189, 193, 194),
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
