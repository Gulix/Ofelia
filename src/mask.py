class mask:
    def __init__(self):
        self.masked_points = [ ]

    def add_points(self, points):
        if not points or len(points) <= 0:
            return
        self.masked_points.extend(points)

    def get_mask(self):
        return self.masked_points