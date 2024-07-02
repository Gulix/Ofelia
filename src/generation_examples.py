import visualizer_image as vis
from colors import palettes
from colors.palettes import paletteColorManager
import mask
import mazePlane as plane


colors = paletteColorManager(colors=palettes._PASTELS_PALETTE)
xMax = 25
yMax = 25
cell_size = 4
path_size = 2

# Only one
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NONE)
maze.add_path((0, 0), starting=True)
maze.add_path((0, yMax - 1), starting=True)
maze.add_path((xMax - 1, 0), starting=True)
maze.add_path((xMax - 1, yMax - 1), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/none.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/none_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Near first origin
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.LEFT_THEN_TOP)
maze.add_path((xMax - 1, 0), starting=True)
maze.add_path((xMax - 1, yMax - 1), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/leftthentop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/leftthentop_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Change the palette
colors = paletteColorManager(colors=palettes._GREEK_PALETTE)

# Near first origin
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN)
maze.add_path((int(xMax / 2), int(yMax / 2)), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/neartrueorigin.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/neartrueorigin_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Near previous position
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_PREVIOUS)
maze.add_path((0, 0), starting=True)
maze.add_path((0, yMax - 1), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/nearprevious.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/nearprevious_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# Change the palette
colors = paletteColorManager(colors=palettes._RAINBOW_PALETTE)

# Full random
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.FULL_RANDOM)
maze.add_path((0, 0), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/fullrandom.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/fullrandom_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)

# With a mask
testMask = mask.mask()
testMask.set_mask_from_image(image='./examples/mask_example.jpg', square_size=(cell_size, cell_size))
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, mask=testMask)
maze.add_path((0, 0), starting=True)
maze.add_path((xMax - 1, yMax - 1), starting=True)
maze.generate()
vis.draw_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examples/mask.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
vis.draw_maze_gif(maze, frame_duration=30, loop=0, image_filename='./examples/mask_loop.gif', \
                  colors=colors, cell_size=cell_size, path_size=path_size)
