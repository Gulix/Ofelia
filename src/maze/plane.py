from enum import Enum
import maze.path as path
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
                 mask:mask.mask = None, branches_probability = None, with_loop = False, random_seed:int = None):
        self.x_size = x_size
        self.y_size = y_size
        self.points = np.zeros((x_size, y_size), dtype=bool) # List of points that are taken (False=Available) 
        self.paths = [ ]
        self.starting_paths = [ ]
        self.new_path_policy = new_path_policy
        self.mask = mask
        if self.mask:
            self.apply_mask()
        self.with_branches = False
        if branches_probability:
            self.with_branches = True
            self.branches_probabilty = branches_probability
        self._with_loop = with_loop
        self._randomizer = random.Random()
        self._randomizer.seed(random_seed)
        self._current_step = 0

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
        rdm_point = self._randomizer.choice(available_points)
        return (rdm_point[0], rdm_point[1])
    
    def generate(self):
        '''generate the structure from the paths'''
        while self._expand_one_step():
            print ("Step " + str(self._current_step), end="\r")
        print(str(self._current_step) + " steps done")
    
    def _expand_one_step(self):
        '''expand the maze by one step. All the active paths grow one more step, and eventually new paths are created.'''
        
        all_paths_done = True
        self._current_step += 1
        for path in self.paths:
            if not path.isDone:
                all_paths_done = False
                # Expand can return multiple points if there is branch
                newPoints = path.expand(self, step = self._current_step)
                if len(newPoints) > 0: # new points have been added
                    for newPoint in newPoints:
                        self.points[newPoint] = True
                else: # A new path is needed
                    newStart = self.getAvailableStart(former_path=path)
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
                if former_path:
                    origin = former_path.get_origin_point()
                    if origin:
                        return self._get_nearest_available( ( origin.get_X(), origin.get_Y() ) )
                return None
            case NewPathPosition.NEAR_TRUE_ORIGIN:
                # Look for the nearest point to the source of the first path from this branch
                if former_path:
                    origin = former_path.get_parent_origin()
                    if origin:
                        return self._get_nearest_available( ( origin.get_X(), origin.get_Y() ) )
                return None
            case NewPathPosition.FULL_RANDOM:
                return self._get_random_available()
            case _: # To expand
                return None

    def add_path(self, xy_coords, parent=None, starting=False, tag=None):
        """add a new path to the maze plane, starting at the given coords"""
        # taking the point of origin
        # it needs to be available
        good_origin = xy_coords
        if self.points[xy_coords]:
            good_origin = self.getAvailableStart(former_path=None)
            if not good_origin:
                good_origin = self._get_nearest_available(xy_coords)
                if not good_origin:
                    return                
        self.points[good_origin] = True
        # the new Path
        branches_prob = None
        if self.with_branches:
            branches_prob = self.branches_probabilty
    
        newPath = path.mazePath(good_origin[0], good_origin[1], \
                                    branches_probability = branches_prob, with_loop=self._with_loop, \
                                    step = self._current_step, \
                                    tag=parent.get_tag() if parent else tag) # TODO : how to use the Tag ?
        newPath.parent = parent
        self.paths.append(newPath)
        if starting:
            self.starting_paths.append(newPath)
        
    def apply_mask(self, mask:mask.mask = None):
        if mask:
            self.mask = mask
        
        for masked_point in self.mask.get_mask():
            self.points[masked_point] = True

    def get_randomizer(self):
        return self._randomizer
    
    def get_final_step(self):
        return self._current_step
