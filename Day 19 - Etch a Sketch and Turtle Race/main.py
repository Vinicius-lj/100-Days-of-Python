from turtle import Turtle, Screen
from random import choice, randint

s = Screen()

# Turtle Race App

s.setup(width=500, height=400)
player_bet = s.textinput(
    title="Player's Bet", prompt="Which of the turtles do you think is gonna win? ")
colors = ["blue", "red", "yellow", "orange", "green", "pink"]
turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.up()
    turtles.append(new_turtle)
y = -100
for x in range(6):
    turtles[x].goto(-230, y)
    y += 40

game_is_on = True
while game_is_on:
    chosen_turtle = choice(turtles)
    chosen_turtle.forward(randint(1, 10))
    finish_line = chosen_turtle.xcor()
    if finish_line > 230:
        game_is_on = False
        winner_color = chosen_turtle.pencolor()
        if winner_color == player_bet:
            print("You win!")
        else:
            print("You lose.")
        print(f"The winner is the {winner_color} turtle")


# Etch a Sketch App

t = Turtle()


def forward():
    return t.forward(20)


def backward():
    return t.backward(20)


def turn_lef():
    return t.left(15)


def turn_right():
    return t.right(15)


def clear_screen():
    return t.reset()


s.onkeypress(forward, "w")
s.onkeypress(backward, "s")
s.onkeypress(turn_lef, "a")
s.onkeypress(turn_right, "d")
s.onkeypress(clear_screen, "c")

s.listen()

s.exitonclick()
