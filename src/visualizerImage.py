from mazePlane import *
from PIL import Image, ImageDraw

def _get_image_from_maze(maze: mazePlane, colors: list, bg_color: tuple = (0, 0, 0)):
    """Generates a PIL image object from a mazePlane"""
    # Initialization of the PIL image object 
    im = Image.new('RGB', (maze.xSize * 10, maze.ySize * 10), bg_color)
    draw = ImageDraw.Draw(im)

    # We'll iterate through the colors list for each path
    color_index = 0
    
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
            draw_x = 10 * x + 2
            draw_y = 10 * y + 2
            draw_end_x = 10 * x + 2 + 6
            draw_end_y = 10 * y + 2 + 6
            
            # Liaisons with the previous position
            if (x == previous_x):
                if (y > previous_y):
                    draw_y -= 4
                else:
                    draw_end_y += 4
            elif (y == previous_y):
                if (x > previous_x):
                    draw_x -= 4
                else:
                    draw_end_x += 4
            previous_x = x
            previous_y = y

            # Drawing the rectangle for the position
            draw.rectangle((draw_x, draw_y, draw_end_x, draw_end_y), fill=color)

        # Getting the new color, looping when all colors have been used
        color_index += 1
        if color_index >= len(colors):
            color_index = 0

    return im

def draw_maze(maze, image_filename = 'ofelia_maze.jpg', expand_maze = True):
    """Draw a maze into an image file"""
    
    # Does the maze need to be expanded to its full capacity?
    if expand_maze:
         while maze.expandOneStep():
             pass

    # A Pastel palette
    colors = [
        (158, 194, 223),
        (234, 206, 235),
        (228, 199, 155),
        (175, 191, 240),
        (207, 211, 167),
        (204, 229, 240)
    ]
        
    pil_image = _get_image_from_maze(maze, colors=colors)
    pil_image.save(image_filename, quality=95)

def draw_maze_gif(maze:mazePlane, image_filename = 'ofelia_maze_animated.gif'):
    # A necessary and beautiful palette
    colors = [
        (255, 0, 24),
        (255, 165, 44),
        (255, 255, 65),
        (0, 128, 24),
        (0, 0, 249),
        (134, 0, 125)
    ]
        
    image_frames = [ ]
    image_frames.append(_get_image_from_maze(maze, colors=colors))
    
    while maze.expandOneStep():
        image_frames.append(_get_image_from_maze(maze, colors=colors))
        
    image_frames[0].save(image_filename, save_all=True, append_images=image_frames[1:], optimize=False, duration=30, loop=0)


# Maze parameters
'''
xMax = 100
yMax = 100
maze = mazePlane(xMax, yMax)
maze.addPath((0, 0))
maze.addPath((0, yMax - 1))
maze.addPath((xMax - 1, 0))
maze.addPath((xMax - 1, yMax - 1))


print("## Drawing...")
draw_maze(maze, expand_maze=True)
'''

xMax = 50
yMax = 50
maze = mazePlane(xMax, yMax)
maze.addPath((0, 0))
maze.addPath((0, yMax - 1))
maze.addPath((xMax - 1, 0))
maze.addPath((xMax - 1, yMax - 1))

draw_maze_gif(maze)