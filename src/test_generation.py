import visualizer_image as vis
import colors_manager as colMg
import mask
import mazePlane as plane
from palettable.colorbrewer.qualitative import Dark2_7
from palettable.cubehelix import perceptual_rainbow_16
from palettable.cubehelix import Cubehelix

#colors = colMg.colorManager(colors=colMg._PASTELS_PALETTE)
colors = colMg.colorManager(palettable=Dark2_7)
colors = colMg.colorManager(palettable=perceptual_rainbow_16)
palette = Cubehelix.make(start=0.1, rotation=-0.75, n=32)
colors = colMg.colorManager(palettable=palette)

xMax = 25
yMax = 25
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, branches_probability=1, with_loop=True, random_seed=3)
#maze = plane.mazePlane(xMax, yMax)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
print("starting maze generation")
maze.generate()
print("maze parameters OK")
print("starting to draw it in ... gif mode")
vis.draw_maze_gif(maze, colors=colors, frame_duration=70, loop=0, image_filename='./generated/maze.gif')
print("gif done")
print("starting to draw it in ... png mode")
vis.draw_maze(maze, image_filename='./generated/simple2.png', 
              colors=colors, cell_size=8, path_size=4)
print("png done")
