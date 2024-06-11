import mazePath
import random

class mazePlane:
    """A path going on in the maze"""
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.takenPoints = { }
        self.paths = [ ]

    def isPositionAvailable(self, position):
        '''is position (a tuple representing x,y coordinates) valid (not out of bounds) and available (not on an existing path)'''
        if position[0] < 0 or position[1] < 0 or position[0] >= self.xSize or position[1] >= self.ySize:
            return False
        
        return position not in self.takenPoints
    
    def expandOneStep(self):
        for path in self.paths:
            if not path.isDone:
                newPoint = path.expand(self)
                if newPoint is not None:
                    self.takenPoints[newPoint] = True
                else:
                    newStart = self.getAvailableStart()
                    if newStart:
                        self.addPath(newStart)
                    else:
                        return False
        return True

    def getAvailableStart(self):
        # Need improvement to get start near the start of the path, or on more random locations ?
        for x in range(self.xSize):
            for y in range(self.ySize):
                point = (x, y)
                if point not in self.takenPoints:
                    return point
        return None

    def addPath(self, xyCoords):
        self.takenPoints[xyCoords] = True
        newPath = mazePath.mazePath(xyCoords[0], xyCoords[1])
        self.paths.append(newPath)
    
    

