
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

xstart = -230
ystart = -100
turtle_store = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=xstart,y=ystart)
    turtle_store.append(new_turtle)
    ystart += 40
    


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_store:  
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win! The {winning_colour} turtle is the winner! ")
            else:
                print(f"Sorry you lose. The {winning_colour} turtle is the winner. ")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
