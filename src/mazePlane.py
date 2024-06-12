from enum import Enum
import mazePath
import random

class NewPathPosition(Enum):
    NONE = 0
    LEFT_THEN_TOP = 1
    FULL_RANDOM = 2
    NEAR_PREVIOUS = 3

class mazePlane:
    """A path going on in the maze"""
    def __init__(self, x_size, y_size, new_path_policy: NewPathPosition = NewPathPosition.LEFT_THEN_TOP):
        self.x_size = x_size
        self.y_size = y_size
        self.takenPoints = { }
        self.paths = [ ]
        self.new_path_policy = new_path_policy

    def isPositionAvailable(self, position):
        """is position (a tuple representing x,y coordinates) valid (not out of bounds) and available (not on an existing path)"""
        if position[0] < 0 or position[1] < 0 or position[0] >= self.x_size or position[1] >= self.y_size:
            return False
        
        return position not in self.takenPoints
    
    def expandOneStep(self):
        for path in self.paths:
            if not path.isDone:
                newPoint = path.expand(self)
                if newPoint is not None:
                    self.takenPoints[newPoint] = True
                else:
                    newStart = self.getAvailableStart(path)
                    if newStart:
                        self.addPath(newStart)
                    else:
                        return False
        return True

    def getAvailableStart(self, former_path):
        # Need improvement to get start near the start of the path, or on more random locations ?
        match self.new_path_policy:
            case NewPathPosition.LEFT_THEN_TOP:
                for x in range(self.x_size):
                    for y in range(self.y_size):
                        point = (x, y)
                        if point not in self.takenPoints:
                            return point
                return None
            case NewPathPosition.NONE:
                return None
            case _: # To expand
                return None

    def addPath(self, xyCoords):
        self.takenPoints[xyCoords] = True
        newPath = mazePath.mazePath(xyCoords[0], xyCoords[1])
        self.paths.append(newPath)
    

