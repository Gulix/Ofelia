from mazePlane import *
from PIL import Image, ImageDraw

def _get_image_from_maze(maze: mazePlane, colors: list, bg_color: tuple = (0, 0, 0), cell_size=10, path_size=6):
    """Generates a PIL image object from a mazePlane"""
    # Initialization of the PIL image object 
    im = Image.new('RGB', (maze.x_size * cell_size, maze.y_size * cell_size), bg_color)
    draw = ImageDraw.Draw(im)

    # We'll iterate through the colors list for each path
    color_index = 0
    
    # Size of the elements
    margin_size = (cell_size - path_size) / 2

    # Iterating through the paths
    for path in maze.paths:

        # Getting the colors        
        color = colors[color_index]
        
        previous_x = -1
        previous_y = -1
        # Drawing each position, one after the other, by getting the positions
        for positions in path.getPositions():
            # Setting the coordinates
            x = positions[0]
            y = positions[1]
            draw_x = cell_size * x + margin_size
            draw_y = cell_size * y + margin_size
            draw_end_x = cell_size * x + margin_size + path_size
            draw_end_y = cell_size * y + margin_size + path_size
            
            # Liaisons with the previous position
            if (x == previous_x):
                if (y > previous_y):
                    draw_y -= margin_size * 2
                else:
                    draw_end_y += margin_size * 2
            elif (y == previous_y):
                if (x > previous_x):
                    draw_x -= margin_size * 2
                else:
                    draw_end_x += margin_size * 2
            previous_x = x
            previous_y = y

            # Drawing the rectangle for the position
            draw.rectangle((draw_x, draw_y, draw_end_x, draw_end_y), fill=color)

        # Getting the new color, looping when all colors have been used
        color_index += 1
        if color_index >= len(colors):
            color_index = 0

    return im

def draw_maze(maze, image_filename = 'ofelia_maze.jpg', expand_maze = True, colors = [ (255, 0, 0) ], \
              cell_size = 10, path_size = 6):
    """Draw a maze into an image file"""
    
    # Does the maze need to be expanded to its full capacity?
    if expand_maze:
         while maze.expandOneStep():
             pass    
        
    pil_image = _get_image_from_maze(maze, colors=colors, cell_size=cell_size, path_size=path_size)
    pil_image.save(image_filename, quality=95)

def draw_maze_gif(maze:mazePlane, image_filename = 'ofelia_maze_animated.gif', \
                  frame_duration:int = 30, loop:int = 0,\
                    colors = [ (169, 13, 42)] ):
            
    image_frames = [ ]
    image_frames.append(_get_image_from_maze(maze, colors=colors))
    
    while maze.expandOneStep():
        image_frames.append(_get_image_from_maze(maze, colors=colors))
    
    # The last one!
    image_frames.append(_get_image_from_maze(maze, colors=colors))
        
    # Save as a gif
    image_frames[0].save(image_filename, save_all=True, append_images=image_frames[1:], optimize=False, duration=frame_duration, loop=loop)


