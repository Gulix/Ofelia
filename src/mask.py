from PIL import Image
import numpy as np

class mask:
    def __init__(self):
        self.masked_points = [ ]

    def add_points(self, points):
        if not points or len(points) <= 0:
            return
        self.masked_points.extend(points)

    def get_mask(self):
        return self.masked_points
    
    def set_mask_from_image(self, image, square_size = (10, 10)):
        # Open image
        im = Image.open(image)
        # Make Numpy array from pixels
        ni = np.array(im)
        
        # Mask pixels where all color < 50 (near black)
        reds = ni[:,:,0]<50
        greens = ni[:,:,1]<50
        blues = ni[:,:,2]<50
        mask = np.logical_and(np.logical_and(reds,greens), blues)
        
        # The maze is not an image : it's a plane with square
        # We define, in the mask, what is the size of a cell (which matches a cell in the plane)
        percent_limit = 0.50
        threshold = square_size[0] * square_size[1] * percent_limit
        
        rows_count = int(ni.shape[0] / square_size[0])
        cols_count = int(ni.shape[1] / square_size[1])
        
        masked_cells = [ ]
        for y in range(0, rows_count):
            for x in range(0, cols_count):
                x_index = x * square_size[0]
                y_index = y * square_size[1]
                cell_mask = mask[y_index:y_index+square_size[1], x_index:x_index+square_size[0]]
                nb_mask = np.count_nonzero(cell_mask)
                if nb_mask >= threshold:
                    masked_cells.append((x, y))
                
        self.masked_points.extend(masked_cells)