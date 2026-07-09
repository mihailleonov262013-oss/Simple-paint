from turtle import *

t1 = Turtle() 
t1.shape('circle')
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
def  color1():
    t1.color('aqua')
scr.onkey(color1 , 'r')
def color2():
    t1.color('red')
scr.onkey(color2, 't')
def color3():
    t1.color('green')
scr.onkey(color3, 'y')
def start_fill():
    t1.begin_fill()
scr.onkey(start_fill, 'u')
def endfill():
    t1.end_fill()
scr.onkey(endfill, 'i')


