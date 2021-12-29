
from turtle import *
import random

yertle = Turtle()
yertle.shape('arrow')
yertle.speed("fastest")
yertle.penup()
yertle.hideturtle()
colours_list  = ["#69FFF1","#2A324B","#EE6352","#F03A47","#E4FF1A", "#BA3B46", "#ED9B40", "#363946", "#139A43", "#0FA3B1"]

yertle.setheading(225)
yertle.fd(300)
yertle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    yertle.dot(20, random.choice(colours_list))
    yertle.fd(50)

    if dot_count % 10 == 0:
        yertle.setheading(90)
        yertle.fd(50)
        yertle.setheading(180)
        yertle.fd(500)
        yertle.setheading(0)

screen = Screen()
screen.exitonclick()