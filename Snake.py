from tkinter import *
import time
from random import randint
main = Tk()
main.title("Snake")
winwidth = 800
winheight = 600
c = Canvas(main, width=winwidth,height=winheight, bg="black")
c.pack()
position = [winwidth/2, winheight/2]
coords = [position]
direction="up"
fruit = [randint(20,int(winwidth/20))*20, randint(20,int(winheight/20))*20]
def left(event):
    global direction
    direction="left"
def right(event):
    global direction
    direction="right"
def up(event):
    global direction
    direction="up"
def down(event):
    global direction
    direction="down"
main.bind("<Left>", left)
main.bind("<Right>", right)
main.bind("<Up>",up)
main.bind("<Down>",down)

while True:
    c.delete("all")
    c.create_rectangle(position[0], position[1], position[0]-20, position[1]-20, fill="White")
    c.create_rectangle(fruit[0],fruit[1],fruit[0]-20,fruit[1]-20,fill="red")
    time.sleep(0.1)
    if direction == "up":
        position[1] -= 20
    elif direction == "down":
        position[1] += 20
    elif direction == "left":
        position[0] -= 20
    elif direction == "right":
        position[0] += 20
    if position[0]==fruit[0] and position[1]==fruit[1]:
        fruit = [randint(20,int(winwidth/20))*20, randint(20,int(winheight/20))*20]
        coords+=position
    c.update()
