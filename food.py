import turtle
from turtle import Turtle
import random

COLOURS = ["CadetBlue", "brown1", "chartreuse4", "CornflowerBlue", "DarkOrange", "DarkOrchid", "DeepPink",
           "aquamarine3", "chocolate2", "DarkGoldenrod1", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

SHAPES = ["circle", "triangle", "turtle"]


class Food(Turtle):
    turtle.colormode(255)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        hold_of_color = self.color()[0]
        self.shape(random.choice(SHAPES))
        self.change_colour()
        self.goto(random_x, random_y)
        return hold_of_color

    def change_colour(self):
        self.color(random.choice(COLOURS))
