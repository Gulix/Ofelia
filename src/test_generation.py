import visualizer_image as vis
import colors_manager as colMg
import mask
import mazePlane as plane


colors = colMg.colorManager(colors=colMg._PASTELS_PALETTE)

xMax = 100
yMax = 75
testMask = mask.mask()
testMask.set_mask_from_image(image='./generated/mask_origin.jpg', square_size=(4,4))
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, mask=testMask)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze(maze, image_filename='./generated/mask.png', colors=colors, cell_size=4, path_size=2)
#vis.draw_maze_gif(maze, frame_duration=30, loop=1, image_filename='./generated/maze.gif')

testMask = mask.mask()
testMask.set_mask_from_image(image='./generated/mask_inverted.jpg', square_size=(4,4))
maze = plane.mazePlane(xMax, yMax, new_path_policy=plane.NewPathPosition.NEAR_TRUE_ORIGIN, mask=testMask)
maze.add_path((0, 0))
maze.add_path((0, yMax - 1))
maze.add_path((xMax - 1, 0))
maze.add_path((xMax - 1, yMax - 1))
vis.draw_maze(maze, image_filename='./generated/mask_2.png', colors=colors, cell_size=4, path_size=2)
