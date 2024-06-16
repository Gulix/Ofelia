import visualizer_image as vis
import mask
import mazePlane as plane

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

# A Pastel palette
colors_pastel = [
    (158, 194, 223),
    (234, 206, 235),
    (228, 199, 155),
    (175, 191, 240),
    (207, 211, 167),
    (204, 229, 240)
]
# A greek palette
colors_greek = [
    (255,255,255),
    (255,246,143),
    (205,102,0),
    (139,37,0)
]
# A rainbow palette
colors_rainbow = [
    (255, 0, 24),
    (255, 165, 44),
    (255, 255, 65),
    (0, 128, 24),
    (0, 0, 249),
    (134, 0, 125)
]

xMax = 100
yMax = 75
testMask = mask.mask()
#testMask.add_points([(24,24), (24,25), (24,26), (25,24), (25,25), (25,26), (26,24), (26,25), (26,26)])
testMask.set_mask_from_image(image='./generated/mask_origin.jpg', square_size=(4,4))
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, mask=testMask)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze(maze, image_filename='./generated/mask.png', colors=colors_greek, cell_size=4, path_size=2)
#vis.draw_maze_gif(maze, frame_duration=30, loop=1, image_filename='./generated/maze.gif')

xMax = 50
yMax = 50
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN)
maze.add_path((25, 25))
#vis.draw_maze_gif(maze, frame_duration=30, loop=1, image_filename='./generated/centeredmaze.gif', colors=colors_pastel)

vis.draw_maze(maze, image_filename='./generated/maze.png', colors=colors_greek, cell_size=10, path_size=4)


