# Run this script, spot the difference between the shape this scripts generates and the shape we generated in class (see class_exercise.py).
# Which one looks better to you?
# Task: look at the code below, and try to explain how it works. Add some more colours in the change_colour function.
# You can also mess around with the numbers the for loop.
# Save your changes in this file and commit changes to submit your homework.
# It works by importing a arrow on a little screen which you can give commands to change hwo it moves, its shape and many more
# To run this script:
# Since we use a new module called turtle, regular python compiler websites (like online-python.com) will not work.
# Please test your script in turtle supported online python environments, like
# "https://pythonsandbox.com/turtle"
# or "https://trinket.io/turtle"
# or "https://stepindev.com/en/py-playground"

import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("square")
t.color("red")
t.speed(0)
t.pensize(15)
t.pencolor("black")
screen.bgcolor("lime")

def change_colour(colour):
    if colour == "red":
        return "green"
    if colour == "green":
        return "orange"
    if colour == "orange":
        return "purple"
    if colour == "purple":
        return "red"

current_colour = "red"

for i in range(100):
    current_colour = change_colour(current_colour)
    t.pencolor(current_colour)
    t.forward(65)
    t.left(89)
    t.forward(75)
    t.left(80)
screen.exitonclick()
