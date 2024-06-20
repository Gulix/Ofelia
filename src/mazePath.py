import random
from maze_points import mazePoint

class mazePath:
    """A path going on in the maze"""
    def __init__(self, xStart, yStart, branches_probability = None, with_loop = False):
        
        # Will store the "current points", from where to expand (we can retrace the path through parent)
        self._all_points = [ mazePoint(None, (xStart, yStart)) ]
        self._active_points = [ self._all_points[0] ]
        self.isDone = False
        self.parent = None
        # Branches
        self.with_branches = False
        if branches_probability:
            self.with_branches = True
            self.branches_probability = branches_probability
        # Loop
        self._with_loop = with_loop
        
    def get_points(self): # To deprecate
        return self._points;
    
    def expand(self, mazePlane):
        """Expand the path one step in an available random direction (or stop it)"""
        new_points = [ ]
        # Multiple active points means multiple active branches
        for expandable_point in self._active_points:

            # The available positions from the current point are strict NWSE neighbours
            neighbour_coords = [
                ( expandable_point.get_X() + 1, expandable_point.get_Y()),
                ( expandable_point.get_X(), expandable_point.get_Y() + 1),
                ( expandable_point.get_X() - 1, expandable_point.get_Y()),
                ( expandable_point.get_X(), expandable_point.get_Y() - 1)
            ]
            
            # Removing the points that might have been taken, in the same step, by a previous branch
            # Those points are not "taken" already, so the is_position_available doesn't take them into concern
            # if loops are authorized, this is a control we don't have to do
            if not self._with_loop:
                for pt in new_points:
                    new_coord = ( pt.get_X(), pt.get_Y() )
                    while new_coord in neighbour_coords: neighbour_coords.remove(new_coord)
            
            # Checking the availability of the points
            available_positions = [ ]
            for coord in neighbour_coords:
                # Making loop with another point of the path (TODO : and then ending path)
                if self._with_loop and self._is_point_in_path(coord):
                    available_positions.append(coord)
                elif mazePlane.is_position_available(coord):
                    available_positions.append(coord)

            # If any position is available
            if len(available_positions) > 0:
                nb_extensions = 1
                # Generating a branch ?
                if self.with_branches and len(available_positions) > 1:
                    if random.randrange(0, 101) <= self.branches_probability:
                        nb_extensions += 1
            
                random.shuffle(available_positions)
                for index in range(0, nb_extensions):
                    new_points.append(mazePoint(expandable_point, available_positions[index]))

        # No new points found? That path is "Done"
        if len(new_points) == 0:
            self.isDone = True
        
        # Refreshing the points table (all & current)
        self._active_points = [ ]
        returned_coords = [ ]
        if len(new_points) > 0:
            self._all_points.extend(new_points)
            self._active_points.extend(new_points)
            for pt in new_points:
                returned_coords.append( (pt.get_X(), pt.get_Y()) )
        
        return returned_coords
    
    def get_origin_point(self):
        return self._all_points[0]

    def get_parent_origin(self):
        """Get the origin of the elder parent from this branch of path"""
        if self.parent:
            return self.parent.get_parent_origin()
        return self.get_origin_point()
    
    def _is_point_in_path(self, coords):
        for pt in self._all_points:
            if pt.get_X() == coords[0] and pt.get_Y() == coords[1]:
                return True
            
        return False
