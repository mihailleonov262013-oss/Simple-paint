from turtle import *

t1 = Turtle() 

def draw(x,y):
    t1.goto(x,y)
t1.ondrag(draw)
def move(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
scr = t1.getscreen()
scr.onscreenclick(move)
scr.listen()
def upp():
    t1.forward(5)
scr.onkey(upp , 'Up')
def down():
    t1.goto(t1.xcor() , t1.ycor() - 5)
scr.onkey(down , 'Down')
def left():
    t1.left(90)
    t1.forward(5)
scr.onkey(left , 'Left')
def right():
    t1.right(90)
    t1.forward(5)
scr.onkey(right , 'Right')
def  colorr():
    t1.color('aqua')
scr.onkey(colorr , 'r')

