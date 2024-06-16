from enum import Enum
import mazePath
import mask
import random
import numpy as np

class NewPathPosition(Enum):
    NONE = 0
    LEFT_THEN_TOP = 1
    FULL_RANDOM = 2
    NEAR_PREVIOUS = 3
    NEAR_TRUE_ORIGIN = 4

class mazePlane:
    """A path going on in the maze"""
    def __init__(self, x_size, y_size, new_path_policy: NewPathPosition = NewPathPosition.LEFT_THEN_TOP,\
                 mask:mask.mask = None):
        self.x_size = x_size
        self.y_size = y_size
        self.points = np.zeros((x_size, y_size), dtype=bool) # List of points that are taken (False=Available) 
        self.paths = [ ]
        self.new_path_policy = new_path_policy
        self.mask = mask
        if self.mask:
            self.apply_mask()

    def is_position_available(self, position):
        """is position (a tuple representing x,y coordinates) valid (not out of bounds) and available (not on an existing path)"""
        # out of bounds
        if position[0] < 0 or position[1] < 0 or position[0] >= self.x_size or position[1] >= self.y_size:
            return False
        
        return not self.points[position]

    def _get_nearest_available(self, origin): 
        '''returns one of the nearest points of origin, which needs to be available'''
        # all available points into a table
        available_points = np.transpose(np.where(~self.points))
        if len(available_points) <= 0:
            return None
               
        origin_point = np.array(origin)
        # Looking for the distance between the two tables
        distances = np.linalg.norm(available_points-origin_point, axis=1)
        min_index = np.argmin(distances)
        return (available_points[min_index][0], available_points[min_index][1])

    def _get_random_available(self):
        '''returns a random available point'''
        # all available points into a table
        available_points = np.transpose(np.where(~self.points))
        if len(available_points) <= 0:
            return None
        rdm_point = random.choice(available_points)
        return (rdm_point[0], rdm_point[1])
    
    def expandOneStep(self):
        for path in self.paths:
            all_paths_done = True
            if not path.isDone:
                all_paths_done = False
                newPoint = path.expand(self)
                if newPoint is not None:
                    self.points[newPoint] = True
                else:
                    newStart = self.getAvailableStart(path)
                    if newStart:
                        self.add_path(newStart, parent=path)
                    else:
                        return False
        return not all_paths_done

    def getAvailableStart(self, former_path):
        """Finds the best available start, depending on the policy defined for the path"""
        # Need improvement to get start near the start of the path, or on more random locations ?
        match self.new_path_policy:
            case NewPathPosition.LEFT_THEN_TOP:
                # Search for an available spot of the left part, starting top, and iterating to right
                for x in range(self.x_size):
                    for y in range(self.y_size):
                        point = (x, y)
                        if self.is_position_available(point):
                            return point
                return None
            case NewPathPosition.NONE:
                # Just one path, then stop
                return None
            case NewPathPosition.NEAR_PREVIOUS:
                # Look for the nearest point to the source of the previous path
                origin = former_path.get_origin()
                if origin:
                    return self._get_nearest_available(origin)
                return None
            case NewPathPosition.NEAR_TRUE_ORIGIN:
                # Look for the nearest point to the source of the first path from this branch
                origin = former_path.get_parent_origin()
                if origin:
                    return self._get_nearest_available(origin)
                return None
            case NewPathPosition.FULL_RANDOM:
                return self._get_random_available()
            case _: # To expand
                return None

    def add_path(self, xy_coords, parent=None):
        """add a new path to the maze plane, starting at the given coords"""
        # taking the point of origin
        self.points[xy_coords] = True
        # the new Path
        newPath = mazePath.mazePath(xy_coords[0], xy_coords[1])
        newPath.parent = parent
        self.paths.append(newPath)
        
    def apply_mask(self, mask:mask.mask = None):
        if mask:
            self.mask = mask
        
        for masked_point in self.mask.get_mask():
            self.points[masked_point] = True

