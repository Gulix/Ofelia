import mazePlane
import random

def displayCharPath(maze, colored=False):
    charIndex = ord('a')
    pathMap = [ ]
    for y in range(maze.ySize):
        pathMap.append([ ])
        for x in range(maze.xSize):
            pathMap[y].append('O')

    for path in maze.paths:
        charVal = chr(charIndex)
        if colored:
            color = list(random.choices(range(256), k=3))
            charVal = '\x1b[' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + \
                'm' + charVal + '\x1b[0m'
        
        for positions in path.getPositions():
            pathMap[positions['y']][positions['x']] = charVal
        charIndex += 1

    for y in range(maze.ySize):
        line = ''
        for x in range(maze.xSize):
            line += pathMap[y][x] + ' '
        print(line)

maze = mazePlane.mazePlane(10, 10) # Size of the maze
# Starting points
maze.addPath(0, 0)
maze.addPath(0, 9)
maze.addPath(9, 0)
maze.addPath(9, 9)
while maze.expandOneStep():
    pass

displayCharPath(maze, colored=False)