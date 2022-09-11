from turtle import Turtle,Screen
from random import randint

screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)
race_is_on = False
colours = ["red","orange","yellow","green","blue","purple"]
count = 50
turtle_list = []


for i in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(x=-240, y=(200 - count))
    turtle_list.append(new_turtle)
    count +=50


if user_bet:
    race_is_on = True
while race_is_on:
    for turtle in turtle_list:
        rand_dist = randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.pencolor() == user_bet:
                print(f"{turtle.color()[0]} won the race and so did you!!")
            else:
                print(f"you lost :({turtle.color()[0]} won the race ")






screen.exitonclick()