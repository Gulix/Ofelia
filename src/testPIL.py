import mazePlane
from PIL import Image, ImageDraw

def drawMaze(maze):
    

    im = Image.new('RGB', (maze.xSize * 10, maze.ySize * 10), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    colors = [ 
        (215, 43, 78),
        (170, 146, 13),
        (133, 155, 248),
        (38, 128, 138),
        (154, 44, 58),
        (25, 117, 111),
        (52, 62, 230),
        (164, 152, 61),
        (222, 11, 128),
        (147, 151, 248),
        (26, 158, 134),
        (11, 79, 124),
        (97, 81, 212),
        (147, 77, 16),
        (64, 163, 133),
        (15, 141, 199),
        (195, 44, 39),
        (146, 79, 3),
        (9, 94, 155),
        (154, 15, 106)
    ]
    colors = [
        (158, 194, 223),
        (234, 206, 235),
        (228, 199, 155),
        (175, 191, 240),
        (207, 211, 167),
        (204, 229, 240)
    ]
    colors = [
        (247, 37, 133),
        (181, 23, 158),
        (114, 9, 183),
        (86, 11, 173),
        (72, 12, 168),
        (58, 12, 163),
        (63, 55, 201),
        (67, 97, 238),
        (72, 149, 239),
        (76, 201, 240)
    ]
    
    
    colorIndex = 0
    
    print(str(len(maze.paths)) + " paths to draw...")

    indexPath = 1
    for path in maze.paths:
        print("Path " + str(indexPath) + "/" + str(len(maze.paths)))
        indexPath += 1
        color = colors[colorIndex]
        
        previousX = -1
        previousY = -1
        for positions in path.getPositions():
            x = positions['x']
            y = positions['y']
            drawX = 10 * x + 2
            drawY = 10 * y + 2
            drawEndX = 10 * x + 2 + 6
            drawEndY = 10 * y + 2 + 6
            if (x == previousX):
                if (y > previousY):
                    drawY -= 4
                else:
                    drawEndY += 4
            elif (y == previousY):
                if (x > previousX):
                    drawX -= 4
                else:
                    drawEndX += 4
            previousX = x
            previousY = y

            draw.rectangle((drawX, drawY, drawEndX, drawEndY), fill=color)

        
        colorIndex += 1
        if colorIndex >= len(colors):
            colorIndex = 0
    
    im.save('ofelia_maze.jpg', quality=95)


xMax = 20
yMax = 20
maze = mazePlane.mazePlane(xMax, yMax)
maze.addPath(0, 0)
maze.addPath(0, yMax - 1)
maze.addPath(xMax - 1, 0)
maze.addPath(xMax - 1, yMax - 1)

print("## Building...")
while maze.expandOneStep():
    pass

print("## Drawing...")
drawMaze(maze)