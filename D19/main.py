from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

donatello = Turtle(shape="turtle")
michelangelo = Turtle(shape="turtle")
leonardo = Turtle(shape="turtle")
raphael = Turtle(shape="turtle")
splinter = Turtle()
shredder = Turtle(shape="triangle")

racers = [donatello, michelangelo, leonardo, raphael, splinter, shredder]
colors = ["purple", "orange", "blue", "red", "grey", "black"]
y_positions = [100, 70, 40, 10, -20, -50]
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which ninja turtle will win the race?")
print(user_bet)



for racer_index in range(0, 6):
    racers[racer_index].penup()
    racers[racer_index].color(colors[racer_index])
    racers[racer_index].goto(x=-230, y=y_positions[racer_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winner = racer
            print(f"The winner is {winner}!")

        random_distance = random.randint(0,10)
        racer.forward(random_distance)





screen.exitonclick()
