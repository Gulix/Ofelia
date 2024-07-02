class gradientColorManager:
    """Class to manage colors when displaying the Ofelia maze. Produces a gradient."""

    def __init__(self, start_color=(0, 0, 0), end_color=(255, 255, 255), steps=36):
        self._current_color_index = 0
        # Making the Gradient (should be enhanced, this is a first draft)
        self._colors = [ ]
        difference = (end_color[0] - start_color[0], end_color[1] - start_color[1], end_color[2] - start_color[2])
        for step in range(0, steps+1):
            if step == 0:
                self._colors.append(start_color)
            else:
                r = start_color[0] + int((step * difference[0]) / steps)
                g = start_color[1] + int((step * difference[1]) / steps)
                b = start_color[2] + int((step * difference[2]) / steps)
                self._colors.append((r, g, b))
            
            
    
    def get_next_color(self):
        
        if self._current_color_index >= len(self._colors):
            self._current_color_index = 0
        color = self._colors[self._current_color_index]
        
        self._current_color_index += 1
        return color
    
    def reset(self):
        self._current_color_index = 0