import turtle

def intro_example():
 """This is only an example method for printing hello"""
 print ("hello")


def draw_petal():
    # Draws a single petal/leaf of a flower by repeatedly moving
    # forward and turnng right 45 degrees.
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    # Draws a single flower using the previous function - petal_draw.
    # It turns 45 degrees and draws a petal four times, and at the
    # end, it darws the stalk.
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance():
    # Draws a single flower and moves to the location of the next
    # flower to be drawn.
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    # Initialize the location of the turtle and draws
    # a bed of 3 flowers
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done()