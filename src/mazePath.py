import random

class mazePath:
    """A path going on in the maze"""
    def __init__(self, xStart, yStart):
        self.points = [ { "x": xStart, "y": yStart }]
        self.isDone = False
        
    def getPositions(self):
        return self.points;
    
    def expand(self, mazePlane):
        """Expand the maze one step in an available random direction (or stop it)"""
        lastPosition = self.points[-1]
        nextPositions = [
            { "x": lastPosition['x'] + 1, "y": lastPosition['y'] },
            { "x": lastPosition['x'], "y": lastPosition['y'] + 1 },
            { "x": lastPosition['x'] - 1, "y": lastPosition['y'] },
            { "x": lastPosition['x'], "y": lastPosition['y'] - 1 }
        ]
        random.shuffle(nextPositions)
        for nextPosition in nextPositions:
            if mazePlane.isPositionAvailable(nextPosition):
                self.points.append(nextPosition)
                return nextPosition
        self.isDone = True
        return None
