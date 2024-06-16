import visualizer_image as vis
import colors_manager as colMg
import mask
import mazePlane as plane


colors = colMg.colorManager(colors=colMg._PASTELS_PALETTE)
xMax = 25
yMax = 25
cell_size = 4
path_size = 2

# Only one
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NONE)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/none.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
# A reset could be good ^^
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/none_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Near first origin
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.LEFT_THEN_TOP)
maze.add_path((xMax - 1, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/leftthentop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/leftthentop_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Change the palette
colors = colMg.colorManager(colors=colMg._GREEK_PALETTE)

# Near first origin
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN)
maze.add_path((int(xMax / 2), int(yMax / 2)))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/neartrueorigin.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/neartrueorigin_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Near previous position
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_PREVIOUS)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/nearprevious.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/nearprevious_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Change the palette
colors = colMg.colorManager(colors=colMg._RAINBOW_PALETTE)

# Full random
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.FULL_RANDOM)
maze.add_path((0, 0))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/fullrandom.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/fullrandom_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# With a mask
testMask = mask.mask()
testMask.set_mask_from_image(image='./examples/mask_example.jpg', square_size=(cell_size, cell_size))
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, mask=testMask)
maze.add_path((0, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./example/mask.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./example/mask_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
