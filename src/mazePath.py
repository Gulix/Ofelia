import random

class mazePath:
    """A path going on in the maze"""
    def __init__(self, xStart, yStart, branches_probability = None):
        self.points = [ (xStart, yStart) ]
        self.current_points = [ (xStart, yStart) ]
        self.isDone = False
        self.parent = None
        self.with_branches = False
        if branches_probability:
            self.with_branches = True
            self.branches_probability = branches_probability
        
    def getPositions(self):
        return self.points;
    
    def expand(self, mazePlane):
        """Expand the path one step in an available random direction (or stop it)"""
        
        new_current_positions = [ ]
        for lastPosition in self.current_points:
            # The available positions from the current point
            nextPositions = [
                ( lastPosition[0] + 1, lastPosition[1]),
                (lastPosition[0], lastPosition[1] + 1),
                (lastPosition[0] - 1, lastPosition[1]),
                (lastPosition[0], lastPosition[1] - 1)
            ]
            available_positions = [ ]
            for nextPosition in nextPositions:
                if mazePlane.is_position_available(nextPosition):
                    available_positions.append(nextPosition)
            
            if len(available_positions) > 0:
                nb_extensions = 1
                # Revealing a branch ?
                if self.with_branches and len(available_positions) > 1:
                    if random.choice([0, 100]) <= self.branches_probability:
                    #if len(self.points) == 10:
                        nb_extensions += 1
            
                random.shuffle(available_positions)
                for index in range(0, nb_extensions):
                    new_current_positions.append(available_positions[index])
            
        if len(new_current_positions) == 0:
            self.isDone = True
        self.current_points = new_current_positions
        self.points.extend(new_current_positions)
        return new_current_positions
    
    def get_origin(self):
        return self.points[0]

    def get_parent_origin(self):
        """Get the origin of the elder parent from this branch of path"""
        if self.parent:
            return self.parent.get_parent_origin()
        return self.get_origin()
