import turtle

turtle.color("Black")
turtle.fillcolor("White")
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
x=-300
y=300
# Global Variables

def pixelSizePicker(pixelSize):
    if (int(pixelSize) > 30):
        ValueError
    elif (int(pixelSize) < 15):
        ValueError
    else:
       return pixelSize
# Function for choosing the number of Pixel Size

def numOfPixelsPerRowPicker(numOfPixelsPerRow):
    if (int(numOfPixelsPerRow) > 30):
        ValueError
    elif (int(numOfPixelsPerRow) < 1):
        ValueError
    else:
       return numOfPixelsPerRow
# Function for choosing the number of Pixels Per Row

def numOfPixelsPerColumnPicker(numOfPixelsPerColumn):
    if (int(numOfPixelsPerColumn) > 30):
        ValueError
    elif (int(numOfPixelsPerColumn) < 1):
        ValueError
    else:
       return numOfPixelsPerColumn
# Function for choosing the number of Pixels Per Column

def starterFunction():
    firstV=int(pixelSizePicker(input("Enter the size of the pixel you want (Min: 15, Max: 30): ")))
    secondV=int(numOfPixelsPerRowPicker(input("Enter the number of pixels you want per row (Min: 1, Max: 30): ")))
    thirdV=int(numOfPixelsPerColumnPicker(input("Enter the number of pixels you want per column (Min: 1, Max: 30): ")))
    global x
    global y
    global PIXEL_SIZE
    global ROWS
    global COLUMNS
    x=-((firstV*secondV))/2
    y=((firstV*secondV))/2
    PIXEL_SIZE = firstV
    ROWS = secondV
    COLUMNS = thirdV
# Function for initially configuring proper settings 

def reposition(x1,y1,headingV):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setheading(headingV)
# Function for deciding positions along with heading

def colorChoice():
    colors = list(input("0 - Black \n1 - White \n2 - Red \n3 - Yellow \n4 - Orange \n5 - Green \n6 - Yellow Green \n7 - Sienna \n8 - Tan \n9 - Gray \nA - Dark Gray \n Please enter a character(s) to choose the colors (You may need to enter an additional input for confirmation): "))
    return colors
# Function for prompting the user to input characters and can be used everywhere.

def pixelColoring(colors):
    chosenColor = colors.pop(0)
    if (chosenColor=="0"):
            turtle.fillcolor("black")
    elif (chosenColor=="1"):
            turtle.fillcolor("white")
    elif (chosenColor=="2"):
            turtle.fillcolor("red")
    elif (chosenColor=="3"):
            turtle.fillcolor("yellow")
    elif (chosenColor=="4"):
            turtle.fillcolor("orange")
    elif (chosenColor=="5"):
            turtle.fillcolor("green")
    elif (chosenColor=="6"):
            turtle.fillcolor("yellowgreen")
    elif (chosenColor=="7"):
            turtle.fillcolor("sienna")
    elif (chosenColor=="8"):
            turtle.fillcolor("tan")
    elif (chosenColor=="9"):
            turtle.fillcolor("gray")
    elif (chosenColor=="A"):
            turtle.fillcolor("darkgray")
    else:
        ValueError
# Function responsible for coloring the pixel based on the input in the colorChoice() function

def customPixel(colors1):
    pixelColoring(colors1)
    turtle.begin_fill()
    for i in range(4):    
        turtle.forward(PIXEL_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
# Function used for drawing and filling the color of the pixel.

def lineDrawing(colors2):
    for w in range(len(colorChoice())):
        customPixel(colors2)
# Function to draw a straight line with its length based on the number of characters inputed.

def customRows(colors3):
    for z in range(ROWS):
        customPixel(colors3)
# Function for creating the rows based on the current value of the global variable

def pixart():
    for u in range(COLUMNS):
        customRows(colorChoice())
        global y
        y=y-PIXEL_SIZE
        reposition(x,y,0)
# Function for creating the entire grid by drawing multiple rows based on the current value of the global variable

def drawingMode():
    drawingMode = input("Choose the drawing mode you'd like to use (SingleLine, PixArt): ")
    if (drawingMode=="PixArt"):
        starterFunction()
        pixart()
    elif (drawingMode=="SingleLine"):
        lineDrawing(colorChoice())
    else:
        print("Mode unsupported :(")
    return False
# Function which provides choice of using 'drawing modes' instead of the user having to look into the code

def main():
    turtle.tracer(False)
    reposition(x,y,0)
    drawingMode()
    turtle.tracer(True)
    reposition(0,0,0)
    turtle.hideturtle()
# Main function which contains the most minimal of details to run all functions in the most efficient way possible.

main()
turtle.exitonclick()
