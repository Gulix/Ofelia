import visualizer_image as vis
import colors_manager as colMg
import mask
import mazePlane as plane


colors = colMg.colorManager(colors=colMg._PASTELS_PALETTE)

xMax = 50
yMax = 50
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NONE, branches_probability=10)
maze.add_path((0, 0))
vis.draw_maze(maze, image_filename='./generated/branches.png', 
              colors=colors, cell_size=4, path_size=2, expand_maze=True)
#vis.draw_maze_gif(maze, frame_duration=30, loop=1, image_filename='./generated/maze.gif')

