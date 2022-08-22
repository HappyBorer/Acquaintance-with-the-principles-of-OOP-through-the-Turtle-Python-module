from turtle import *
from random import randint
from time import *

screen = Screen() # вывод в  окно
colormode(255) # чтобы можно было в RGB указывать цвет

finish = 200
t1 = Turtle()
t1.shape('turtle')
t1.color(randint(0, 255), randint(0, 255), randint(0, 255))
t1.penup()
t1.goto(-200, 20)
t1.pendown()
t1.speed(1)

t2 = Turtle()
t2.shape('turtle')
t2.color(randint(0, 255), randint(0, 255), randint(0, 255))
t2.penup()
t2.goto(-200, -20)
t2.pendown()
t2.speed(1)

def razmetka():
    t = Turtle()
    #t.color('black')
    t.speed(0)
    for i in range(1, 21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown
        t.goto(-200+i*20, -100)
        
    t.hideturtle()

razmetka()

def catch1(x, y):
    t1.write('Ouch!', font = ('Arial', 14, 'normal'))
    t1.fd(randint(10, 15))
    
t1.onclick(catch1)

def catch2(x, y):
    t2.write('Ouch!', font = ('Arial', 14, 'normal'))
    t2.fd(randint(10, 15))
    
t2.onclick(catch2)

while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2, 7))
    t2.forward(randint(2, 7))
    sleep(0.05)

screen.exitonclick() # задержка окна






