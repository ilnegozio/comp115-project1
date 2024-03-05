
import turtle
import random


def star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(5):
        t.forward(size)
        t.right(144) # angle of turn

def draw_star(t, num_stars):
    for i in range(num_stars):
        x = random.randint(-450, 450) # star's coordinates are randomly generated
        y = random.randint(-450, 450)
        size = random.randint(1, 4)
        star(t, x, y, size)

def create_drawing():
    x1 = random.randint(-200, 200) # determine position for the figure 
    y1 = random.randint(-200, 200)
    drawing.penup()
    drawing.left(90)
    drawing.forward(200)
    drawing.right(90)
    drawing.pendown()
    for i in range(24):
        drawing.forward(100)
        drawing.right(45)
        drawing.forward(50)
        drawing.right(135)
        drawing.forward(50)
        drawing.right(45)
        drawing.forward(50)
        drawing.right(135)
        drawing.right(15)  # adjust the angle for the next petal

def main():
    screen = turtle.Screen() # define screen to edit
    screen.setup(width=900, height=900)
    screen.bgcolor("black")
    screen.title("stars in space") # title for the window
    create_drawing()
    draw_star(t, 200) # number can be changed anytime
    t.hideturtle() # hide for the final picture
    drawing.hideturtle()
    screen.mainloop() # keep the window open

t = turtle.Turtle()
t.speed(0) # set to fastest speed
t.color("white")

drawing = turtle.Turtle()
drawing.speed(0)
drawing.color("red")

main() # call the function
