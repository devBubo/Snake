from tkinter import Tk, Canvas
from random import randint
root = Tk()
root.title("Snake - Score: {} points".format(0))
canvas = Canvas()
winwidth = 640
winheight = 640
canvas.config(width=winwidth, height=winheight,bg="black")
canvas.pack()


grid_size = 20
a = winwidth / grid_size

snake_x = [5, 4, 3]
snake_y = [5, 5, 5]

apple = [randint(0, grid_size - 1), randint(0, grid_size - 1)]

dx = 1
dy = 0
score = 0
direction = "right"

#drawing objects
def draw_square(column, row, color):
    canvas.create_rectangle(column * a, row * a, (column + 1) * a, (row + 1) * a, fill=color, outline="gray")
def draw_apple():
    draw_square(apple[0], apple[1], "red")
def draw():
    canvas.delete('all')

    for i in range(len(snake_x)):
        draw_square(snake_x[i], snake_y[i], "#0eff00")

#moves snake
def move():
    x = snake_x[0]
    y = snake_y[0]
    snake_x.insert(0, (x + dx) % grid_size)
    snake_y.insert(0, (y + dy) % grid_size)
    snake_x.pop()
    snake_y.pop()

#binding controls
def up(e):
    global dx, dy, direction
    if direction != "down":
        dx = 0
        dy = -1
        direction = "up"
def down(e):
    global dx, dy, direction
    if direction != "up":
        dx = 0
        dy = 1
        direction = "down"
def right(e):
    global dx, dy, direction
    if direction != "left":
        dx = 1
        dy = 0
        direction = "right"
def left(e):
    global dx, dy, direction
    if direction != "right":
        dx = -1
        dy = 0
        direction = "left"

canvas.bind_all('<Up>', up)
canvas.bind_all('<Down>', down)
canvas.bind_all('<Right>', right)
canvas.bind_all('<Left>', left)

#mainloop
def animation():
    global score, apple
    move()
    draw()
    draw_apple()
    for j in range(1,len(snake_x)):
        if snake_x[j] == snake_x[0] and snake_y[j] == snake_y[0]:
            print("You lost with a score of {}".format(score))
            quit()
    if snake_x[0] == apple[0] and snake_y[0] == apple[1]:
        snake_x.append(apple[0])
        snake_y.append(apple[1])
        rx = randint(0, grid_size - 1)
        ry = randint(0, grid_size - 1)
        while True:
            for k in range(len(snake_x)):
                if snake_x[k] == rx and snake_y[k] == ry:
                    rx = randint(0, grid_size - 1)
                    ry = randint(0, grid_size - 1)
                    break
            break
        apple = [randint(0, grid_size - 1), randint(0, grid_size - 1)]
        score+=1
        root.title("Snake - Score: {} points".format(score))
    canvas.after(50, animation)



animation()
canvas.mainloop()