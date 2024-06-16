import random

class mazePath:
    """A path going on in the maze"""
    def __init__(self, xStart, yStart):
        self.points = [ (xStart, yStart) ]
        self.isDone = False
        self.parent = None
        
    def getPositions(self):
        return self.points;
    
    def expand(self, mazePlane):
        """Expand the path one step in an available random direction (or stop it)"""
        lastPosition = self.points[-1]
        nextPositions = [
            ( lastPosition[0] + 1, lastPosition[1]),
            (lastPosition[0], lastPosition[1] + 1),
            (lastPosition[0] - 1, lastPosition[1]),
            (lastPosition[0], lastPosition[1] - 1)
        ]
        random.shuffle(nextPositions)
        for nextPosition in nextPositions:
            if mazePlane.is_position_available(nextPosition):
                self.points.append(nextPosition)
                return nextPosition
        self.isDone = True
        return None
    
    def get_origin(self):
        return self.points[0]

    def get_parent_origin(self):
        """Get the origin of the elder parent from this branch of path"""
        if self.parent:
            return self.parent.get_parent_origin()
        return self.get_origin()
