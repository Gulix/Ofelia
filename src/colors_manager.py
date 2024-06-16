_GREEK_PALETTE = [ (255,255,255), (255,246,143), (205,102,0), (139,37,0) ]
_PASTELS_PALETTE = [ (158, 194, 223), (234, 206, 235), (228, 199, 155), (175, 191, 240), (207, 211, 167), (204, 229, 240) ]
_RAINBOW_PALETTE = [ (255, 0, 24), (255, 165, 44), (255, 255, 65), (0, 128, 24), (0, 0, 249), (134, 0, 125) ]

class colorManager:
    """Simple class to manage colors when displaying the Ofelia maze. A looped list of colors."""

    def __init__(self, colors = [ (169, 13, 13) ]):
        self._colors = colors
        self._current_color_index = -1
    
    def get_next_color(self):
        
        if self._current_color_index >= len(self._colors):
            self._current_color_index = 0
        color = self._colors[self._current_color_index]
        
        self._current_color_index += 1
        return color


