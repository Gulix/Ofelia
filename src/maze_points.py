class mazePoint:
    def __init__(self, parent = None, coords = (0, 0)):
        self._parent = parent
        self._coords = coords
        self._children = [ ]
        if parent:
            parent._children.append(self)

    def get_position(self):
        return self._coords
    
    def is_origin(self):
        return not self._parent
    
    def get_X(self):
        return self._coords[0]
    
    def get_Y(self):
        return self._coords[1]
    
    def get_coords(self):
        return self._coords
    
    def get_parent(self):
        return self._parent    
    
    def get_children(self):
        return self._children
