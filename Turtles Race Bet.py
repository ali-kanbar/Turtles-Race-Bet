from turtle import *
from random import randint
import time
from tkinter import messagebox

def distance_generator():
    return randint(1,10)
def index_generator():
    return randint(0,6)

screen = Screen()
screen.tracer(0)
screen.setup(width=500,height=400)
turtles = []
bet = ""
max_x = -230
colors = ["red", "green", "blue", "yellow", "orange", "purple","black"]
distances = [-230]*7
y = 150
line = Turtle()
line.width(5)
line.penup()
line.goto(x = 230,y = 200)
line.pendown()
line.rt(90)
for _ in range(15):
    line.fd(20)
    line.penup()
    line.fd(10)
    line.pendown()
    
for i in range(7):
    t = Turtle()
    t.penup()
    t.shape("turtle") 
    t.color(colors[i])
    t.goto(x = -230,y=y)
    y -= 50
    turtles += [t]
screen.update()
while bet.lower() not in colors:
    bet = screen.textinput(title = "Make Your Bet",prompt = "Which turtle will win the race?Enter a color : ")
ind = colors.index(bet)
screen.tracer(1)
while max_x < 210:
    time.sleep(0.01)
    distance = distance_generator()
    index = index_generator()
    distances[index] += distance
    turtles[index].fd(distance)
    if distances[index] > max_x:max_x = distances[index]
if index == ind:messagebox.showinfo(title = "yeyy",message ="you won the bet")
else:messagebox.showinfo(title ="Oops!",message = "you lost the bet,"+colors[index]+" won")

screen.exitonclick()