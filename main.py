import movement
import world_tools
import helper
import config
import farming_logic

movement.go_to_default_pos()
last_x = 5
last_y = 5

while True:
    farming_mode = config.farming_mode
    grid = farming_logic.get_grid_from_farming_mode(farming_mode)
    matrix = helper.generate_grid_matrix(grid)

    farming_logic.planter(matrix)
    farming_logic.harvester(grid)
    movement.go_to_default_pos()
