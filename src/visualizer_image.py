from mazePlane import *
from colors_manager import colorManager
from PIL import Image, ImageDraw

def _get_image_from_maze(maze: mazePlane, colors:colorManager , bg_color: tuple = (0, 0, 0), cell_size=10, path_size=6):
    """Generates a PIL image object from a mazePlane"""
    # Initialization of the PIL image object 
    im = Image.new('RGB', (maze.x_size * cell_size, maze.y_size * cell_size), bg_color)
    draw = ImageDraw.Draw(im)

    # Size of the elements
    margin_size = (cell_size - path_size) / 2

    # Iterating through the paths
    for path in maze.paths:

        # Getting the colors        
        color = colors.get_next_color()
        
        origin = path.get_origin_point()
        _draw_point_then_children(origin, drawing_canvas=draw, cell_size=cell_size, path_size=path_size, color=color)

    return im

def _draw_point_then_children(point, drawing_canvas, color, cell_size=10, path_size=6):
    
    # Size of the elements
    margin_size = (cell_size - path_size) / 2
    
    # Get Drawing coords
    x = point.get_X()
    y = point.get_Y()
    draw_x = cell_size * x + margin_size
    draw_y = cell_size * y + margin_size
    draw_end_x = cell_size * x + margin_size + path_size - 1 # -1 because inclusive bounds
    draw_end_y = cell_size * y + margin_size + path_size - 1
    
    # Liaisons with the previous point
    parent = point.get_parent()
    if parent:
        if (x == parent.get_X()):
            if (y > parent.get_Y()):
                draw_y -= margin_size * 2
            else:
                draw_end_y += margin_size * 2
        elif (y == parent.get_Y()):
            if (x > parent.get_X()):
                draw_x -= margin_size * 2
            else:
                draw_end_x += margin_size * 2

    # Draw the rectangle
    drawing_canvas.rectangle((draw_x, draw_y, draw_end_x, draw_end_y), fill=color)

    # Draw the children
    for child in point.get_children():
        _draw_point_then_children(child, drawing_canvas=drawing_canvas, cell_size=cell_size, path_size=path_size, color=color)


def draw_maze(maze, colors, image_filename = 'ofelia_maze.jpg', expand_maze = True, \
              cell_size = 10, path_size = 6):
    """Draw a maze into an image file"""
    
    # Does the maze need to be expanded to its full capacity?
    if expand_maze:
         while maze.expand_one_step():
             pass    
        
    pil_image = _get_image_from_maze(maze, colors=colors, cell_size=cell_size, path_size=path_size)
    pil_image.save(image_filename, quality=95)

def draw_maze_gif(maze:mazePlane, colors, image_filename = 'ofelia_maze_animated.gif', \
                  frame_duration:int = 30, loop:int = 0,\
                    cell_size = 10, path_size = 6):
            
    image_frames = [ ]
    image_frames.append(_get_image_from_maze(maze, colors=colors, cell_size=cell_size, path_size=path_size))
    
    while maze.expand_one_step():
        colors.reset()
        image_frames.append(_get_image_from_maze(maze, colors=colors, cell_size=cell_size, path_size=path_size))
    
    # The last one!
    colors.reset()
    image_frames.append(_get_image_from_maze(maze, colors=colors, cell_size=cell_size, path_size=path_size))
        
    # Save as a gif
    if loop is None:
        image_frames[0].save(image_filename, save_all=True, append_images=image_frames[1:], optimize=False, duration=frame_duration)
    else:
        image_frames[0].save(image_filename, save_all=True, append_images=image_frames[1:], optimize=False, duration=frame_duration, loop=loop)
    


