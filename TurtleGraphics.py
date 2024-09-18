#TurtleGraphics.py
#Name: Jace Wilson
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def fillCorner(myTurtle, corner):
    for i in range(1):
        drawSquare(myTurtle, 100)
        if corner == 2:
            myTurtle.forward(50)
        elif corner == 3:
            myTurtle.forward(50)
            myTurtle.right(90)
            myTurtle.penup()
            myTurtle.forward(50)
            myTurtle.pendown()
        elif corner == 4:
            myTurtle.right(90)
            myTurtle.forward(100)
            myTurtle.left(90)
            myTurtle.forward(50)
            myTurtle.left(90)
        #if corner == 4:
            
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()

def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(100)
        myTurtle.right(360 / sides)

def squaresInSquares(myTurtle, num):
    size = 10
    for i in range(num):
        drawSquare(myTurtle, size)
        size = size + 20
        myTurtle.penup()
        myTurtle.left(180)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.pendown()
def main():
    myTurtle = turtle.Turtle()
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
