from turtle import Turtle, Screen
from random import randint, choice
import colorgram
import re

t = Turtle()
screen = Screen()
screen.colormode(255)

# colors = colorgram.extract('hirst.jpg', 15)
# color_list = [tuple(map(int, re.findall(r'\d+', str(color.rgb)))) for color in colors]

filtered_color_list = [(236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192)]

t.pensize(20)
t.speed(0)
pos_y = -235
for x in range(10):
    t.up()
    t.setposition(-235, pos_y)
    for y in range(10):
        t.down()
        t.color(choice(filtered_color_list))
        t.forward(1)
        t.up()
        t.forward(50)
    pos_y += 50

screen.exitonclick()

# Similar Exercises

# def random_color():
#     r =randint(0, 200)
#     g =randint(0, 200)
#     b =randint(0, 200)
#     return (r, g, b)

# for sides in range(3, 50):
#     angle = 360 / sides
#     t.color(random_color())
#     for side in range(sides):
#         t.forward(50)
#         t.right(angle)

# t.pensize(10)
# screen.colormode(255)
# moves = (0, 90, 180, 270)
# t.speed(8)
# for _ in range(300):
#     t.color(random_color())
#     t.setheading(choice(moves))
#     t.forward(50)

# t.speed(0)
# circle_num = 50
# angle = 360 / circle_num
# for _ in range(circle_num):
#     t.color(random_color())
#     t.circle(100)
#     t.right(angle)   
