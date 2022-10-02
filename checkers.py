import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
turtle.fillcolor("White")
turtle.color("Black")

assert (ROWS == COLUMNS)

def reposition(x,y):
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    return x,y

def pixel(color1):
    turtle.fillcolor(color1)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()

def row(color2,color3):
    for z in range(int(ROWS/2)):
        pixel(color2)
        turtle.forward(30)
        pixel(color3)
        turtle.forward(30)

def grid(color4,color5):
    for w in range(int(COLUMNS/2)):
        row(color4,color5)
        turtle.right(90)
        turtle.forward(PIXEL_SIZE*2)
        turtle.right(90)
        row(color4,color5)
        turtle.left(180)

def main():
    turtle.tracer(False)
    reposition(-300,300)
    grid("Red","Black")
    turtle.tracer(True)

main()
turtle.exitonclick()