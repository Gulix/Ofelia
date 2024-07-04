import visualizer_image as vis
from colors import palettes
from colors.palettes import paletteColorManager
from colors.gradient import gradientColorManager
import mask
import maze.plane as plane
from palettable.colorbrewer.qualitative import Dark2_7
from palettable.cubehelix import perceptual_rainbow_16
from palettable.cubehelix import Cubehelix

#colors = paletteColorManager(colors=colMg._PASTELS_PALETTE)
colors = paletteColorManager(palettable=Dark2_7)
colors = paletteColorManager(palettable=perceptual_rainbow_16)
palette = Cubehelix.make(start=0.1, rotation=-0.75, n=32)
colors = paletteColorManager(palettable=palette)

colors = gradientColorManager()
dic_colors = { }
dic_colors["R"] = gradientColorManager(start_color=(255, 0, 0), end_color=(75, 0, 0), steps=25)
dic_colors["G"] = gradientColorManager(start_color=(0, 255, 0), end_color=(0, 75, 0), steps=25)
dic_colors["B"] = gradientColorManager(start_color=(0, 0, 255), end_color=(0, 0, 75), steps=25)

xMax = 40
yMax = 40
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, branches_probability=1)
maze.add_path(xy_coords=(0, 0), tag='R' )
maze.add_path(xy_coords=(0, yMax - 1), tag='G')
maze.add_path(xy_coords=(xMax - 1, 0), tag='B')
print("starting maze generation")
maze.generate()
print("maze parameters OK")
print("starting to draw it in ... gif mode")
vis.draw_maze_gif(maze, colors=colors, colors_bytag=dic_colors, frame_duration=70, loop=0, image_filename='./generated/maze.gif')
print("gif done")
print("starting to draw it in ... png mode")
vis.draw_maze(maze, image_filename='./generated/simple2.png', 
              colors=colors, colors_bytag=dic_colors, cell_size=8, path_size=4)
print("png done")
