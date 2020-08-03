#created by @ethans33 7/25/2020
import pygame as pg
import numpy as np
from colr import color

#Colors
background_color = (222, 222, 222)
rectColor = (255, 255, 255)

#Grid dimensions
gridWidth = 35
gridDimensions = 20
gridLineWidth = 2
(width, height) = (
    gridWidth * gridDimensions + (gridLineWidth * gridDimensions) + gridLineWidth, 
    gridWidth * gridDimensions + (gridLineWidth * gridDimensions) + gridLineWidth)

#Screen
screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.set_caption("Snake")
pg.display.flip()
fps = 13
fpsClock = pg.time.Clock()


#create grid
gridColors = {}

for a in range(gridDimensions):
    for b in range(gridDimensions):
        gridColors.update({(a, b): (255, 255, 255)})

def clearGrid():
    for a in range(gridDimensions):
        for b in range(gridDimensions):
            gridColors[(a, b)] = (255, 255, 255)

def drawGrid():
    x, y = gridLineWidth, gridLineWidth

    for a in range(gridDimensions):
        for b in range(gridDimensions):
            pg.draw.rect(screen, gridColors[(a, b)], (x, y, gridWidth, gridWidth))
            x += gridWidth + gridLineWidth
        x = gridLineWidth
        y += gridWidth + gridLineWidth

running = True
frame = 0

class Snake:
    color = (255, 0, 100)
    length = 3

    speed = {
        "x": 0,
        "y": 0
    }
    location = {
        "x": 7,
        "y": 7,
        "history": []
    }

class Apple:
    location = {
        "x": 1,
        "y": 1
    }
    color = (66, 245, 200)

def gameover():
    Snake.location["x"] = gridDimensions // 2
    Snake.location["y"] = gridDimensions // 2
    Snake.location["history"] = []
    Snake.length = 3
    Apple.location["x"] = 1
    Apple.location["y"] = 1

def controls():
    if event.type == pg.KEYDOWN:
        if event.key==pg.K_UP:
            if Snake.speed["x"] != 1:
                Snake.speed["y"] = 0
                Snake.speed["x"] = -1
        elif event.key==pg.K_LEFT:
            if Snake.speed["y"] != 1:
                Snake.speed["x"] = 0
                Snake.speed["y"] = -1
        elif event.key==pg.K_DOWN:
            if Snake.speed["x"] != -1:
                Snake.speed["y"] = 0
                Snake.speed["x"] = 1
        elif event.key==pg.K_RIGHT:
            if Snake.speed["y"] != -1:
                Snake.speed["x"] = 0
                Snake.speed["y"] = 1

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    drawGrid()
    clearGrid()

    if len(Snake.location["history"]) > Snake.length:
        Snake.location["history"].pop(0)

    Snake.location["history"].append((Snake.location["x"], Snake.location["y"]))
    Snake.location["x"] += Snake.speed["x"]
    Snake.location["y"] += Snake.speed["y"] 

    #Color Snake Location
    for i in Snake.location["history"]:
        gridColors[(i[0], i[1])] = Snake.color
    gridColors[(Snake.location["x"], Snake.location["y"])] = Snake.color
    
    #Color Apple Location
    gridColors[(Apple.location["x"], Apple.location["y"])] = Apple.color

    #Apple Eaten
    if Snake.location["x"] == Apple.location["x"] and Snake.location["y"] == Apple.location["y"]:
        Apple.location["x"] = np.random.randint(gridDimensions)
        Apple.location["y"] = np.random.randint(gridDimensions)
        Snake.length += 1
        print(color("An apple has been eaten!", fore="pink", back=(27, 25, 87)))
        print(color("Your length is " + str(Snake.length), fore="pink", back=(27, 25, 87)))
    
    #Loop over history
    for i in Snake.location["history"]:
        if  Snake.location["x"] == i[0] and Snake.location["y"] == i[1]:
            gameover()

        while Apple.location["x"] == i[0] and Apple.location["y"] == i[1]:
            Apple.location["x"] = np.random.randint(gridDimensions)
            Apple.location["y"] = np.random.randint(gridDimensions)
    
    #Bounds
    if Snake.location["x"] > gridDimensions or Snake.location["x"] < 0 or Snake.location["y"] > gridDimensions or Snake.location["y"] < 0:
        gameover()

    controls()
                
    pg.display.update()
    fpsClock.tick(fps)

events = pg.event.get()

