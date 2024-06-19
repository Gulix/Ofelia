import visualizer_image as vis
import colors_manager as colMg
import mask
import mazePlane as plane


colors = colMg.colorManager(colors=colMg._PASTELS_PALETTE)

xMax = 15
yMax = 15
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, branches_probability=10)
#maze = plane.mazePlane(xMax, yMax)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
vis.draw_maze(maze, image_filename='./generated/simple.png', 
              colors=colors, cell_size=8, path_size=4, expand_maze=True)
#vis.draw_maze_gif(maze, frame_duration=30, loop=1, image_filename='./generated/maze.gif')

