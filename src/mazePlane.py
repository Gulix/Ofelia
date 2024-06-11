import mazePath
import random

class mazePlane:
    """A path going on in the maze"""
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.takenPoints = [ ]
        self.paths = [ ]

    def isPositionAvailable(self, position):
        if position['x'] < 0 or position['y'] < 0 or position['x'] >= self.xSize or position['y'] >= self.ySize:
            return False
        
        return position not in self.takenPoints
    
    def expandOneStep(self):
        for path in self.paths:
            if not path.isDone:
                newPoint = path.expand(self)
                if newPoint is not None:
                    self.takenPoints.append(newPoint)
                else:
                    newStart = self.getAvailableStart()
                    if newStart:
                        self.addPath(newStart['x'], newStart['y'])
                    else:
                        return False
        return True

    def getAvailableStart(self):
        for x in range(self.xSize):
            for y in range(self.ySize):
                point = { 'x': x, 'y': y }
                if point not in self.takenPoints:
                    return point
        return None

    def addPath(self, xStart, yStart):
        self.takenPoints.append({ 'x': xStart, 'y': yStart })
        newPath = mazePath.mazePath(xStart, yStart)
        self.paths.append(newPath)
    
    def displayCharPath(self, colored=False):
        charIndex = ord('a')
        pathMap = [ ]
        for y in range(self.ySize):
            pathMap.append([ ])
            for x in range(self.xSize):
                pathMap[y].append('O')

        for path in self.paths:
            charVal = chr(charIndex)
            if colored:
                color = list(random.choices(range(256), k=3))
                charVal = '\x1b[' + str(color[0]) + ';' + str(color[1]) + ';' + str(color[2]) + \
                    'm' + charVal + '\x1b[0m'
            
            for positions in path.getPositions():
                pathMap[positions['y']][positions['x']] = charVal
            charIndex += 1

        for y in range(self.ySize):
            line = ''
            for x in range(self.xSize):
                line += pathMap[y][x] + ' '
            print(line)

