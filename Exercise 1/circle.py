import math
import turtle

turtle.speed(0)

r = 100
accuracy = 2 * 360
angle = (2 * math.pi * r)/accuracy
length = (2 * math.pi * r)/accuracy

def draw_circle():
    turtle.up()
    go_to_start_point()

    turtle.down()
    draw_circle_parts()

    turtle.done()

def go_to_start_point():
    turtle.right(180)
    turtle.forward(r)

def draw_circle_parts():
    for i in range(0, accuracy):
        turtle.right(angle)
        turtle.forward(length)

if __name__ == "__main__":
    draw_circle()