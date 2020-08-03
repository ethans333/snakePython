# snakePython
I breakdown what It takes to build the game Snake in python.

```python
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
```
